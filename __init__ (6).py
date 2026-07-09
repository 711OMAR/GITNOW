"""Auth: email/JWT plus OAuth (Google/GitHub) entrypoints. Scaffolded."""
from __future__ import annotations

from datetime import datetime, timedelta

import jwt
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ...core.config import settings

router = APIRouter()


class LoginRequest(BaseModel):
    email: str
    password: str


def _issue_token(sub: str) -> str:
    exp = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    return jwt.encode({"sub": sub, "exp": exp}, settings.secret_key, algorithm="HS256")


@router.post("/login")
async def login(req: LoginRequest) -> dict:
    # Replace with a real user store + password hashing (argon2) + 2FA check.
    if not req.email or not req.password:
        raise HTTPException(400, "email and password required")
    return {"access_token": _issue_token(req.email), "token_type": "bearer"}


@router.get("/oauth/{provider}/start")
async def oauth_start(provider: str) -> dict:
    if provider not in {"google", "github"}:
        raise HTTPException(404, "unknown provider")
    # Return the provider authorize URL in a real implementation.
    return {"provider": provider, "authorize_url": f"https://oauth.example/{provider}"}
