"""Minimal database readiness probe.

The ORM (SQLAlchemy) and migrations (Alembic) arrive in Milestone 2; this module only
checks that the configured database is reachable and has PostGIS enabled.
"""

from dataclasses import dataclass

import psycopg

from safarnama_api.config import Settings


@dataclass(frozen=True)
class DatabaseStatus:
    ok: bool
    postgis_version: str | None = None
    error: str | None = None


def check_database(settings: Settings) -> DatabaseStatus:
    if settings.database_url is None:
        return DatabaseStatus(ok=False, error="database_not_configured")
    try:
        with (
            psycopg.connect(
                settings.database_url.get_secret_value(),
                connect_timeout=settings.database_connect_timeout_seconds,
            ) as conn,
            conn.cursor() as cur,
        ):
            cur.execute("SELECT postgis_version()")
            row = cur.fetchone()
    except psycopg.errors.UndefinedFunction:
        return DatabaseStatus(ok=False, error="postgis_not_installed")
    except psycopg.Error:
        # Do not leak connection details (host, user) to API clients.
        return DatabaseStatus(ok=False, error="database_unavailable")
    return DatabaseStatus(ok=True, postgis_version=str(row[0]) if row else None)
