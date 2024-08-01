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

def add_application_to_db(job_id, application_information):
  with engine.connect() as conn:
    query = text("INSERT INTO application (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

    conn.execute(query, {"job_id": job_id, "full_name": application_information['full_name'], "email": application_information['email'], "linkedin_url": application_information['linkedin_url'], "education": application_information['education'], "work_experience": application_information['work_experience'], "resume_url": application_information['resume_url']})