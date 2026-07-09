"""Manage OSINT sources: list status, enable/disable, set keys."""
from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel

from ...sources.registry import registry

router = APIRouter()


@router.get("")
async def list_sources() -> list[dict]:
    return registry.status()


class ToggleRequest(BaseModel):
    enabled: bool


@router.post("/{slug}/toggle")
async def toggle(slug: str, req: ToggleRequest) -> dict:
    (registry.enable if req.enabled else registry.disable)(slug)
    return {"slug": slug, "enabled": req.enabled}


class KeyRequest(BaseModel):
    api_key: str


@router.post("/{slug}/key")
async def set_key(slug: str, req: KeyRequest) -> dict:
    # NB: the raw key is written to the encrypted vault, never returned.
    registry.set_key(slug, req.api_key)
    return {"slug": slug, "configured": True}
