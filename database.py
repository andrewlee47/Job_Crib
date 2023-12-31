from sqlalchemy import create_engine, text
import os



#connect to cloud database
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


def job_details_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Jobs WHERE id = :val"), {'val': id})

        row = result.fetchone()
        if row is None:
            return None
        else:
            column_names = result.keys()  # Get column names from the result
            job_details = {column: value for column, value in zip(column_names, row)}
            return job_details
