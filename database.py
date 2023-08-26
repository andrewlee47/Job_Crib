
from sqlalchemy import create_engine, text
import os


database_url = os.environ.get('AWS_URL')

engine = create_engine(database_url, pool_pre_ping=True)


def load_jobs_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Jobs"))

        Jobs = []
        column_names = result.keys()  # Get column names from the result

        for row in result:
            job_dict = {column.lower(): value for column, value in zip(column_names, row)}
            Jobs.append(job_dict)
        return Jobs



