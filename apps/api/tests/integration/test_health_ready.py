"""Runs against the local/CI PostGIS database. Select with `pytest -m integration`."""

import os

import pytest
from pydantic import SecretStr

from safarnama_api.config import Settings

from ..conftest import make_client

pytestmark = pytest.mark.integration


def test_readiness_ok_with_postgis() -> None:
    url = os.environ.get("SAFARNAMA_DATABASE_URL")
    if not url:
        pytest.fail("SAFARNAMA_DATABASE_URL must be set for integration tests")
    with make_client(Settings(environment="test", database_url=SecretStr(url))) as client:
        response = client.get("/health/ready")
    assert response.status_code == 200, response.text
    body = response.json()
    assert body["status"] == "ready"
    assert body["database"] == "ok"
    assert body["postgis_version"]
