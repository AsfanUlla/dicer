from starlite import get, BackgroundTask, Response
from typing import Any
from api.schema import ScrapeData
from scrapper.scrapy import Scrapy
import asyncio

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
            count = await ScrapeData.count().where(
                                    #ScrapeData.title.ilike("%"+q+"%"),
                                    ScrapeData.skills.ilike("%"+q+"%"),
                                    ScrapeData.jobLocation.ilike("%"+location+"%")
                                )
            if offset > count:
                offset = 0
            data = await ScrapeData.select()\
                            .where(
                                #ScrapeData.title.ilike("%"+q+"%"),
                                ScrapeData.skills.ilike("%"+q+"%"),
                                ScrapeData.jobLocation.ilike("%"+location+"%")
                            )\
                            .limit(limit)\
                            .offset(offset)\
                            .order_by(
                                getattr(ScrapeData, sort, "id")
                            )
        except Exception as exc:
            print(exc)
    if not data:
        scrape = Scrapy()
        params = {}
        if q != "":
            params["q"] = q
        if location != "":
            params["location"] = location
        message = "Data not Available initiating background scrape job check back in ~ 60Sec"
        if forceScrape:
            message = "Force Starting Scrape Task in Background check back in ~ 60Sec"
        return Response(
            {"message": message},
            background=BackgroundTask(scrape.start_scrape, params=params),
        )

    return Response(data)
