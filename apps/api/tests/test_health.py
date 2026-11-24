import pytest
from fastapi.testclient import TestClient
from pydantic import SecretStr, ValidationError

from safarnama_api.config import Settings

from .conftest import make_client


def test_liveness_ok_without_database(client_without_db: TestClient) -> None:
    response = client_without_db.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_readiness_reports_unconfigured_database(client_without_db: TestClient) -> None:
    response = client_without_db.get("/health/ready")
    assert response.status_code == 503
    body = response.json()
    assert body["status"] == "not_ready"
    assert body["error"] == "database_not_configured"


def test_readiness_hides_connection_details_when_database_unreachable() -> None:
    # Port 1 on localhost refuses connections; nothing external is contacted.
    settings = Settings(
        environment="test",
        database_url=SecretStr("postgresql://user:hunter2@127.0.0.1:1/nope"),
        database_connect_timeout_seconds=1,
    )
    with make_client(settings) as client:
        response = client.get("/health/ready")
    assert response.status_code == 503
    assert response.json()["error"] == "database_unavailable"
    assert "hunter2" not in response.text
    assert "127.0.0.1" not in response.text


def test_invalid_database_url_is_rejected() -> None:
    with pytest.raises(ValidationError):
        Settings(database_url=SecretStr("not-a-dsn"))


def test_database_url_is_not_exposed_in_repr() -> None:
    settings = Settings(database_url=SecretStr("postgresql://u:hunter2@localhost:5433/db"))
    assert "hunter2" not in repr(settings)


def test_cors_origins_parsed_from_comma_separated_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SAFARNAMA_CORS_ORIGINS", "http://localhost:3000, http://127.0.0.1:3000")
    assert Settings().cors_origins == ["http://localhost:3000", "http://127.0.0.1:3000"]
