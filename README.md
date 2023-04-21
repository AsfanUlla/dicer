# Scrapy

- Web Scrapper to scrape jobs data from www.dice.com
   (Note: Indeed kept blocking(403), didn't have enough time to figure it out so went with dice.com which is similar to indeed)
- Api starts scrapping in the background if the data is not available in the local Database this behaviour can also be forced check api docs below

## Prerequisites

- [Postgresql](https://www.postgresql.org/)
- Python 3.10.x

## Installation

```bash
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## DB Configuration

- Modify DB configuration accordingly, located in `piccolo_conf.py`

```python
DB = PostgresEngine(config={
    'host': <db_host>,
    'database': <db_name>,
    'user': <db_user>,
    'password': <db_passwd>
})
```

## Run

```bash
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

#### /jobs? sample response

```json
[
	{
		"id": 1,
		"title": "Backend Java Developer",
		"jobLocation": "Sunnyvale, CA, USA",
		"postedDate": "2023-04-19T15:49:03Z",
		"detailsPageUrl": "https://www.dice.com/job-detail/eaafe54d-3218-45a9-8a2a-05b30c5f091f",
		"companyPageUrl": "https://www.dice.com/company/91009974",
		"salary": "Up to $60",
		"companyName": "Tekcel Consulting Inc",
		"summary": "Position: Backend Java Developer Location: Sunnyvale, CA or Virginia Duration: 12+ Months Work authorization: ,  GC-EAD (Independent Candidates ONLY)   Backend Engineering: You design and build ground-up transformational tools, integrating data across sources and collaborating across cross-functional teams.   Tech Skills: Java, SQL and NoSQL, Service Oriented architecture,  Spring Boot, Open-Source technologies.   Required: Walmart experience Backend Java Development 7+ Years",
		"description": "Position: Backend Java DeveloperLocation: Sunnyvale, CA or VirginiaDuration: 12+ MonthsWork authorization: ,  GC-EAD (Independent Candidates ONLY) Backend Engineering:You design and build ground-up transformational tools, integrating data across sources and collaborating across cross-functional teams. Tech Skills:Java, SQL and NoSQL, Service Oriented architecture,  Spring Boot, Open-Source technologies. Required:Walmart experienceBackendJava Development7+ Years",
		"skills": "Boot,Java,NoSQL,Service Oriented architecture,Backend",
		"jobId": "99a1a7e5faccc56fe28bc4529aed1cec",
		"modifiedDate": "2023-04-19T15:49:03Z",
		"created_at": "2023-04-21T01:43:02.013500"
	}
]
```
