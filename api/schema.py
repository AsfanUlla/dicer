import datetime

from piccolo.columns.column_types import (
    JSON,
    JSONB,
    ForeignKey,
    Integer,
    Varchar,
    Text,
    Timestamp,
    Timestamptz,
    Array
)
from piccolo.table import Table

class ScrapeData(Table):
    title = Text()
    jobLocation = Text()
    postedDate = Timestamptz()
    detailsPageUrl = Text()
    companyPageUrl = Text()
    salary = Text()
    companyName = Text()
    summary = Text()
    description = Text()
    skills = Text()
    #exp_required = Text() # Is generally available in description
    #job_responsibilities = Text() # Is generally available in description
    jobId = Text()
    modifiedDate = Timestamptz()
    created_at = Timestamp(auto_update=datetime.datetime.now)
    
