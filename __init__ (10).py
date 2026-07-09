"""
Source abstraction layer.

Every OSINT provider (Shodan, crt.sh, Wayback, ...) is a subclass of `Source`.
The registry can enable/disable any of them at runtime without the rest of the
app knowing which concrete provider it is talking to. Each source declares:

  * which entity types it can take as INPUT  (e.g. "domain", "ip")
  * which entity types it can PRODUCE        (e.g. "certificate", "subdomain")
  * whether it needs an API key
  * a rate limit

Connectors return a normalized `SourceResult`: a bag of Entities and
Relationships plus the raw payload (cached for provenance / audit).

This platform is for lawful OSINT only: it queries public data sources and
never attempts authenticated access, exploitation, or scraping behind logins.
"""
from __future__ import annotations

import abc
import asyncio
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Iterable

import httpx


class EntityType(str, Enum):
    DOMAIN = "domain"
    IP = "ip"
    EMAIL = "email"
    USERNAME = "username"
    PHONE = "phone"
    HASH = "hash"
    URL = "url"
    COMPANY = "company"
    PERSON = "person"
    WALLET = "wallet"
    DNS = "dns"
    CERTIFICATE = "certificate"
    SERVER = "server"
    ORGANIZATION = "organization"
    SOCIAL = "social"
    REPOSITORY = "repository"
    WEBSITE = "website"


@dataclass
class Entity:
    type: EntityType
    value: str
    attributes: dict[str, Any] = field(default_factory=dict)
    confidence: float = 0.5  # 0..1, used by the risk/confidence scorer

    @property
    def key(self) -> str:
        return f"{self.type.value}:{self.value.lower()}"


@dataclass
class Relationship:
    source: str          # Entity.key
    target: str          # Entity.key
    label: str
    confidence: float = 0.5


@dataclass
class SourceResult:
    source: str
    entities: list[Entity] = field(default_factory=list)
    relationships: list[Relationship] = field(default_factory=list)
    raw: Any = None
    error: str | None = None
    took_ms: int = 0


class Source(abc.ABC):
    """Base class every connector implements."""

    #: unique slug, e.g. "crtsh"
    slug: str = "base"
    #: human name shown in the UI
    name: str = "Base Source"
    #: category used for grouping in the UI ("network", "dns", "reputation", ...)
    category: str = "generic"
    #: does this source need a credential to work?
    requires_key: bool = False
    #: entity types accepted as a query seed
    accepts: tuple[EntityType, ...] = ()
    #: max requests per minute (registry enforces a token bucket)
    rate_limit_per_min: int = 60

    def __init__(self, api_key: str | None = None, enabled: bool = True):
        self.api_key = api_key
        self.enabled = enabled
        self._last_calls: list[float] = []

    # ------- capability checks -------
    def can_handle(self, entity_type: EntityType) -> bool:
        return self.enabled and entity_type in self.accepts and self.is_configured

    @property
    def is_configured(self) -> bool:
        return (not self.requires_key) or bool(self.api_key)

    # ------- rate limiting (simple sliding window) -------
    async def _respect_rate_limit(self) -> None:
        now = time.monotonic()
        self._last_calls = [t for t in self._last_calls if now - t < 60]
        if len(self._last_calls) >= self.rate_limit_per_min:
            sleep = 60 - (now - self._last_calls[0])
            await asyncio.sleep(max(sleep, 0))
        self._last_calls.append(time.monotonic())

    # ------- public entrypoint -------
    async def query(self, entity_type: EntityType, value: str) -> SourceResult:
        started = time.monotonic()
        if not self.can_handle(entity_type):
            return SourceResult(source=self.slug, error="source cannot handle this entity")
        try:
            await self._respect_rate_limit()
            result = await self.fetch(entity_type, value)
        except httpx.HTTPError as exc:
            result = SourceResult(source=self.slug, error=f"http error: {exc}")
        except Exception as exc:  # noqa: BLE001 - surface any connector bug as an error, don't crash the sweep
            result = SourceResult(source=self.slug, error=str(exc))
        result.took_ms = int((time.monotonic() - started) * 1000)
        return result

    # ------- to be implemented by concrete connectors -------
    @abc.abstractmethod
    async def fetch(self, entity_type: EntityType, value: str) -> SourceResult:
        ...

    # ------- shared http helper -------
    async def _get_json(self, url: str, **kwargs) -> Any:
        async with httpx.AsyncClient(timeout=20, follow_redirects=True,
                                     headers={"User-Agent": "AutoMemoriesDoll-OSINT/1.0"}) as client:
            resp = await client.get(url, **kwargs)
            resp.raise_for_status()
            return resp.json()


def dedupe_entities(entities: Iterable[Entity]) -> list[Entity]:
    """Collapse duplicate entities, keeping the highest confidence + merged attrs."""
    merged: dict[str, Entity] = {}
    for e in entities:
        if e.key in merged:
            cur = merged[e.key]
            cur.confidence = max(cur.confidence, e.confidence)
            cur.attributes.update({k: v for k, v in e.attributes.items() if v})
        else:
            merged[e.key] = e
    return list(merged.values())
