# Local development commands. Everything here targets the local machine only.
.DEFAULT_GOAL := help
API := apps/api
LOCAL_DATABASE_URL ?= postgresql://safarnama:safarnama_dev@127.0.0.1:5433/safarnama

.PHONY: help setup db-up db-down db-reset dev-api dev-web lint format typecheck test test-integration check

help: ## List available commands
	@grep -E '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*## "}{printf "  %-18s %s\n", $$1, $$2}'

setup: ## Install web and API dependencies from lockfiles
	pnpm install --frozen-lockfile
	cd $(API) && uv sync --locked

db-up: ## Start local PostGIS (Docker) and wait until healthy
	docker compose up -d --wait db

db-down: ## Stop local PostGIS (keeps data)
	docker compose stop db

db-reset: ## DESTRUCTIVE: delete the local PostGIS container and its data volume
	docker compose down -v

dev-api: ## Run the API with reload on http://127.0.0.1:8000
	cd $(API) && uv run uvicorn safarnama_api.main:app --reload --host 127.0.0.1 --port 8000

dev-web: ## Run the web app on http://localhost:3000
	pnpm dev

lint: ## Lint web (ESLint) and API (Ruff)
	pnpm lint
	cd $(API) && uv run ruff check .

format: ## Format web (Prettier) and API (Ruff)
	pnpm format
	cd $(API) && uv run ruff format .

typecheck: ## Type-check web (tsc) and API (mypy)
	pnpm typecheck
	cd $(API) && uv run mypy

test: ## Unit tests (no database needed)
	pnpm test
	cd $(API) && uv run pytest

test-integration: ## API tests against local PostGIS (run `make db-up` first)
	cd $(API) && SAFARNAMA_DATABASE_URL=$(LOCAL_DATABASE_URL) uv run pytest -m integration

check: ## Everything CI runs, except integration tests and the build
	pnpm format:check
	cd $(API) && uv run ruff format --check .
	$(MAKE) lint typecheck test
