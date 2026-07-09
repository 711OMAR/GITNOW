"""Serves the OSINT source Codex — the curated catalog of tools/sources,
plus the subset that can be promoted to real registry connectors."""
import json
from pathlib import Path
from fastapi import APIRouter

router = APIRouter()
_CATALOG = json.loads(
    (Path(__file__).resolve().parents[2] / "catalog" / "catalog.json").read_text("utf-8")
)


@router.get("")
def get_catalog():
    """Full Codex: every category and tool with metadata."""
    return _CATALOG


@router.get("/connector-candidates")
def connector_candidates():
    """Tools with real APIs, grouped by the entity type they can seed on.
    These map directly onto the source registry — the platform's next
    connectors should come from here."""
    by_type: dict[str, list[dict]] = {}
    for category, tools in _CATALOG["categories"].items():
        for tool in tools:
            if not tool.get("integrable"):
                continue
            for et in tool.get("entity_types", []):
                by_type.setdefault(et, []).append({
                    "name": tool["name"],
                    "category": category,
                    "keyless": tool.get("keyless", False),
                    "description": tool.get("description", ""),
                })
    return {
        "entity_types": sorted(by_type),
        "candidates": by_type,
        "total": sum(len(v) for v in by_type.values()),
    }
