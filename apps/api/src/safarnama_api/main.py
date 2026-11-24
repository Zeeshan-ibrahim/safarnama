from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from safarnama_api.api.routes import health
from safarnama_api.config import Settings, get_settings


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or get_settings()
    app = FastAPI(title="Safarnama API", version="0.1.0")
    if settings.cors_origins:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.cors_origins,
            allow_methods=["GET"],
            allow_headers=["*"],
        )
    app.include_router(health.router)
    return app


app = create_app()
