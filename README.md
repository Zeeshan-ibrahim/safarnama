# Safarnama

A trip planner for domestic travel in Pakistan, built planning-first. Product and architecture documents are in [`docs/`](docs/). Project rules are in [`CLAUDE.md`](CLAUDE.md).

**Status:** Milestone 1 (project foundation). The app has no travel data or features yet.

## Layout

| Path | What |
|---|---|
| `apps/web` | Next.js + TypeScript + Tailwind frontend (pnpm) |
| `apps/api` | FastAPI backend, Python 3.13 (uv) |
| `compose.yaml` | Local PostgreSQL + PostGIS for development only |
| `.github/workflows/ci.yml` | Lint, type-check, test and build on every PR |

## Prerequisites

- Node 24 (see `.nvmrc`), with pnpm via corepack: `corepack enable pnpm`
- [uv](https://docs.astral.sh/uv/). It installs Python 3.13 itself if needed.
- Docker, for the local database

## Setup

```bash
cp .env.example .env     # local placeholders only, never real credentials
make setup               # install web + API dependencies from lockfiles
make db-up               # start local PostGIS on 127.0.0.1:5433
```

## Commands

| Command | Does |
|---|---|
| `make dev-api` | API on http://127.0.0.1:8000 (`/health`, `/health/ready`, `/docs`) |
| `make dev-web` | Web on http://localhost:3000 |
| `make lint` / `make format` / `make typecheck` | ESLint + Ruff / Prettier + Ruff / tsc + mypy |
| `make test` | Unit tests (no database needed) |
| `make test-integration` | API tests against local PostGIS (needs `make db-up`) |
| `make check` | All non-integration CI checks |
| `make db-down` | Stop the database and keep its data |
| `make db-reset` | **Destructive:** delete the local database volume |

`make help` lists all commands.

## Health endpoints

- `GET /health`: liveness check. Always returns 200 if the process is up.
- `GET /health/ready`: returns 200 when the database is reachable and PostGIS is installed, otherwise 503 with an error code. Connection details are never included.

## Safety

Use local and synthetic data only. Nothing in this repo connects to production, cloud or paid services. Never commit `.env` or real credentials.
