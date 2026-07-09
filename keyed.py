"""Search endpoint: run a source sweep for a seed entity."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ...sources.base import EntityType
from ...sources.registry import registry

router = APIRouter()


class SearchRequest(BaseModel):
    entity_type: EntityType
    value: str


@router.post("")
async def search(req: SearchRequest) -> dict:
    if not req.value.strip():
        raise HTTPException(400, "empty query")
    # In production this enqueues a Celery task and streams results over the
    # WebSocket; the synchronous path is kept for small sweeps and tests.
    return await registry.sweep(req.entity_type, req.value.strip())
