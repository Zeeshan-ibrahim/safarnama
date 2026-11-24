from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from safarnama_api.config import Settings, get_settings
from safarnama_api.main import create_app


def make_client(settings: Settings) -> TestClient:
    app = create_app(settings)
    app.dependency_overrides[get_settings] = lambda: settings
    return TestClient(app)


@pytest.fixture
def client_without_db() -> Iterator[TestClient]:
    with make_client(Settings(environment="test", database_url=None)) as client:
        yield client
