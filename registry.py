"""Export an investigation to JSON / CSV / Markdown / STIX 2.1."""
from __future__ import annotations

import json
import uuid
from datetime import datetime

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter()


def to_stix(entities: list[dict], relationships: list[dict]) -> dict:
    """Minimal STIX 2.1 bundle: entities -> observed-data / indicators."""
    objects = []
    for e in entities:
        objects.append({
            "type": "observed-data",
            "id": f"observed-data--{uuid.uuid4()}",
            "spec_version": "2.1",
            "created": datetime.utcnow().isoformat() + "Z",
            "number_observed": 1,
            "objects": {"0": {"type": e.get("type"), "value": e.get("value")}},
        })
    return {"type": "bundle", "id": f"bundle--{uuid.uuid4()}", "objects": objects}


@router.post("/stix", response_class=PlainTextResponse)
async def export_stix(payload: dict) -> str:
    bundle = to_stix(payload.get("entities", []), payload.get("relationships", []))
    return json.dumps(bundle, indent=2)
