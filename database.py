import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
import os

from sqlalchemy.engine import result

db_connection_string = os.environ['DB_CONNECTION_STRING']



engine = create_engine(db_connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs = []
    for row in result.all():
      jobs.append(row._asdict())

  return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"),{"val":id})
    row = result.all()

    if len(row) == 0:
      return None
    else:
      return row[0]._asdict()

print(load_job_from_db(1))