from starlite import get, BackgroundTask, Response
from typing import Any
from api.schema import ScrapeData
from scraper.scrapy import Scrapy
import asyncio
import json
from api.utils import UUIDEncoder

@get("/")
def health_check() -> dict[str, bool]:
    return {"success": True}


@get("/jobs")
async def jobs(
    q: str = "",
    location: str = "",
    sort: str = "id",
    limit: int = 10,
    offset: int = 0,
    forceScrape: bool = False
) -> Response[dict[str, Any]]:
    data = []
    if not forceScrape:
        try:
            data = await ScrapeData.select()\
                            .where(
                                (ScrapeData.title.ilike("%"+q+"%"))\
                                 | (ScrapeData.skills.ilike("%"+q+"%"))\
                                 & (ScrapeData.jobLocation.ilike("%"+location+"%"))
                            )\
                            .columns(ScrapeData.all_columns()[1:])\
                            .limit(limit)\
                            .offset(offset)\
                            .order_by(
                                getattr(ScrapeData, sort, "id")
                            )
        except Exception as exc:
            print(exc)
    if not data:
        params = {}
        if q != "":
            params["q"] = q
        if location != "":
            params["location"] = location
        scrape = Scrapy()
        fresh_jobs_data = await scrape.scrape_search(params=params)
        return Response(
            {
                "message": "Freshly scraped Data",
                "data": fresh_jobs_data
            },
            background=BackgroundTask(scrape.scrape_job, jobs=fresh_jobs_data),
        )
    return Response(
        {
            "message": "Existing Jobs data use forceScrape to force a new scape job",
            "data": data
        }
    )

@get('/reset')
async def reset() -> Response[dict[str, str]]:
    await ScrapeData.delete(force=True)
    return Response(
        {
            "message": "Db Cleared"
        }
    )
