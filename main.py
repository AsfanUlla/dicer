import uvicorn

from pydantic import BaseSettings

from starlite import Starlite, OpenAPIConfig
from starlite.plugins.piccolo_orm import PiccoloORMPlugin
from piccolo.engine import engine_finder
from starlite.middleware import RateLimitConfig

from api.views import jobs, health_check, reset

rate_limit_config = RateLimitConfig(rate_limit=("minute", 20), exclude=["/schema", "/"])

async def get_db_connection() -> None:
    engine = engine_finder()
    await engine.start_connection_pool()


async def close_db_connection() -> None:
    engine = engine_finder()
    await engine.close_connection_pool()

route_handler = [
    jobs,
    health_check,
    reset
]

app = Starlite(
    route_handlers=route_handler, 
    on_startup=[get_db_connection], 
    on_shutdown=[close_db_connection],
    plugins=[PiccoloORMPlugin()],
    middleware=[rate_limit_config.middleware],
    openapi_config=OpenAPIConfig(title="Scrapy API", version="1.0.0"),
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
        port=8000
    )
