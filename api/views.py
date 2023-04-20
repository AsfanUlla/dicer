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
    limit: str = '10',
    offset: str = 0,
    forceScrape: str | None = None
) -> Response[dict[str, Any]]:
    data = []
    try:
        count = await ScrapeData.count().where(
                                #ScrapeData.title.ilike("%"+q+"%"),
                                ScrapeData.skills.ilike("%"+q+"%"),
                                ScrapeData.jobLocation.ilike("%"+location+"%")
                            )
        if int(offset) > count:
            offset = 0
        data = await ScrapeData.select()\
                        .where(
                            #ScrapeData.title.ilike("%"+q+"%"),
                            ScrapeData.skills.ilike("%"+q+"%"),
                            ScrapeData.jobLocation.ilike("%"+location+"%")
                        )\
                        .limit(int(limit))\
                        .offset(int(offset))\
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
        return Response(
            {"data": "Data not Available initiating scrape job check back in ~ 60Sec"},
            background=BackgroundTask(scrape.start_scrape, params=params),
        )

    return Response(data)
