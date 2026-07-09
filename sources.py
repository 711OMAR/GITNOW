"""
Auto Memories Doll — OSINT Atelier API.

FastAPI application factory. Wires routers, CORS, and a WebSocket channel for
live investigation updates. For lawful OSINT over public data only.
"""
from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from .api.routes import auth, investigations, search, sources, exports, catalog
from .core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup: init db pool, warm caches, etc.
    yield
    # shutdown: close pools


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version="1.0.0",
        description="API-first OSINT platform. Public-data intelligence only.",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000", "https://automemoriesdoll.com"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
    app.include_router(search.router, prefix="/api/search", tags=["search"])
    app.include_router(investigations.router, prefix="/api/investigations", tags=["investigations"])
    app.include_router(sources.router, prefix="/api/sources", tags=["sources"])
    app.include_router(exports.router, prefix="/api/exports", tags=["exports"])
    app.include_router(catalog.router, prefix="/api/catalog", tags=["catalog"])

    @app.get("/api/health", tags=["meta"])
    async def health() -> dict:
        return {"status": "ok", "app": settings.app_name}

    @app.websocket("/ws/investigations/{case_id}")
    async def ws(websocket: WebSocket, case_id: str):
        """Push live entity/relationship updates as a sweep runs."""
        await websocket.accept()
        try:
            while True:
                msg = await websocket.receive_json()
                # echo / dispatch to celery task events in a real deployment
                await websocket.send_json({"case": case_id, "ack": msg})
        except WebSocketDisconnect:
            return

    return app


app = create_app()
