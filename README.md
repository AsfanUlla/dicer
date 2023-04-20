# Scrapy

Web Scrapper to scrape jobs data from www.dice.com

## Prerequisites

- [Postgresql](https://www.postgresql.org/)
- Python 3.10.x

## Installation

```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## DB Configuration

- Modify DB configuration accordingly, located in `piccolo_conf.py`

```
DB = PostgresEngine(config={
    'host': <db_host>,
    'database': <db_name>,
    'user': <db_user>,
    'password': <db_passwd>
})
```

## Run

```
python main.py
```

## API Features `/jobs?<params>`

- Fast
- Pagination
- Sort
- Query based on technology and location
- Rate Limit 20/min
- Unit tests
- [Piccolo ORM](https://piccolo-orm.com/)

(Note: Api is designed in such a fasion that if the query result is empty it will initiate a background task to scrape 50 jobs based on the query parameters)

## API Documentation

- OpenAPI Documentation:
  - http://localhost:8000/schema
  - http://localhost:8000/schema/swagger

#### /jobs? query params:

    q                   Jobs search query(technology)
    location            Jobs Location
    sort                sort results based on title|postedDate|modifiedDate|created_at ...
    limit               limit number of results per page
    offset              Offset for pagination
    forceScrape         Force initiates background scraping task overiding the default behaviour
