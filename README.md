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

- Pagination
- Sort
- Query based on technology and location
- Rate Limit 20/min
- Unit tests

(Note: Api is designed in such a fasion that if the query result is empty it will initiate a background task to scrape 50 jobs based on the query parameters)

## API Documentation

//TODO
