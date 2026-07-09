"""CRUD for investigations (correspondences). Persistence stubbed for scaffold."""
from __future__ import annotations

from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Replace with a SQLAlchemy repository; kept in-memory for the scaffold.
_STORE: dict[str, dict] = {}


class InvestigationIn(BaseModel):
    name: str
    seed_type: str
    seed_value: str
    tags: list[str] = []
    notes: str = ""


@router.get("")
async def list_investigations() -> list[dict]:
    return list(_STORE.values())


@router.post("")
async def create(inv: InvestigationIn) -> dict:
    case_id = f"CASE-{len(_STORE)+1:04d}"
    rec = inv.model_dump() | {"id": case_id, "created_at": datetime.utcnow().isoformat()}
    _STORE[case_id] = rec
    return rec


@router.get("/{case_id}")
async def get(case_id: str) -> dict:
    return _STORE.get(case_id, {"error": "not found"})
