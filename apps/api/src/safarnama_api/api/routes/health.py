from typing import Annotated, Literal

from fastapi import APIRouter, Depends, Response, status
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel

from safarnama_api.config import Settings, get_settings
from safarnama_api.db import check_database

router = APIRouter(prefix="/health", tags=["health"])


class LivenessResponse(BaseModel):
    status: Literal["ok"]


class ReadinessResponse(BaseModel):
    status: Literal["ready", "not_ready"]
    database: Literal["ok", "error"]
    postgis_version: str | None = None
    error: str | None = None


@router.get("", response_model=LivenessResponse)
def liveness() -> LivenessResponse:
    """The process is up. Does not touch the database."""
    return LivenessResponse(status="ok")


@router.get(
    "/ready",
    response_model=ReadinessResponse,
    responses={status.HTTP_503_SERVICE_UNAVAILABLE: {"model": ReadinessResponse}},
)
async def readiness(
    response: Response, settings: Annotated[Settings, Depends(get_settings)]
) -> ReadinessResponse:
    """The database is reachable and PostGIS is installed."""
    result = await run_in_threadpool(check_database, settings)
    if not result.ok:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return ReadinessResponse(status="not_ready", database="error", error=result.error)
    return ReadinessResponse(status="ready", database="ok", postgis_version=result.postgis_version)
