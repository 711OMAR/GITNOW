"""
Registry: the single place that knows about every connector.

The API layer never imports a concrete connector. It asks the registry:
    registry.sweep(EntityType.DOMAIN, "example.com")
and gets back the merged results of every ENABLED, CONFIGURED source that can
handle a domain. Enabling/disabling a source is a one-liner and can be driven
from the settings UI / database.
"""
from __future__ import annotations

import asyncio

from ..core.config import settings
from .base import Entity, EntityType, Relationship, Source, SourceResult, dedupe_entities
from .connectors.free import CrtShSource, WaybackSource
from .connectors.keyed import IPinfoSource, ShodanSource, VirusTotalSource

# Add new providers here. Keys come from settings (env / vault).
_ALL_SOURCE_CLASSES = [
    CrtShSource,
    WaybackSource,
    IPinfoSource,
    ShodanSource,
    VirusTotalSource,
]


class SourceRegistry:
    def __init__(self) -> None:
        self._sources: dict[str, Source] = {}
        self._bootstrap()

    def _bootstrap(self) -> None:
        for cls in _ALL_SOURCE_CLASSES:
            key = settings.api_keys.get(cls.slug)
            enabled = settings.enabled_sources.get(cls.slug, True)
            self._sources[cls.slug] = cls(api_key=key, enabled=enabled)

    # ---- management (wire these to the settings API) ----
    def enable(self, slug: str) -> None:
        if slug in self._sources:
            self._sources[slug].enabled = True

    def disable(self, slug: str) -> None:
        if slug in self._sources:
            self._sources[slug].enabled = False

    def set_key(self, slug: str, key: str) -> None:
        if slug in self._sources:
            self._sources[slug].api_key = key

    def status(self) -> list[dict]:
        return [{
            "slug": s.slug, "name": s.name, "category": s.category,
            "enabled": s.enabled, "requires_key": s.requires_key,
            "configured": s.is_configured, "accepts": [a.value for a in s.accepts],
            "rate_limit_per_min": s.rate_limit_per_min,
        } for s in self._sources.values()]

    def handlers_for(self, entity_type: EntityType) -> list[Source]:
        return [s for s in self._sources.values() if s.can_handle(entity_type)]

    # ---- the sweep ----
    async def sweep(self, entity_type: EntityType, value: str) -> dict:
        handlers = self.handlers_for(entity_type)
        results: list[SourceResult] = await asyncio.gather(
            *(s.query(entity_type, value) for s in handlers)
        ) if handlers else []

        entities: list[Entity] = []
        relationships: list[Relationship] = []
        provenance = []
        for r in results:
            entities.extend(r.entities)
            relationships.extend(r.relationships)
            provenance.append({"source": r.source, "took_ms": r.took_ms,
                               "error": r.error, "entities": len(r.entities)})

        return {
            "seed": {"type": entity_type.value, "value": value},
            "entities": [e.__dict__ | {"type": e.type.value} for e in dedupe_entities(entities)],
            "relationships": [rel.__dict__ for rel in relationships],
            "provenance": provenance,
        }


registry = SourceRegistry()
