from flask import Flask, render_template, jsonify
from database import load_jobs_db, job_details_db

app = Flask(__name__)
app.static_folder = 'static'





@app.route("/")
def careerbuilder():
    Job_list = load_jobs_db()
    return render_template('home.html', jobs=Job_list)


@app.route("/job/<id>")
def display_job(id):
    job = job_details_db(id)
    return render_template('jobpage.html', job=job)


@app.route("/api/jobs")
def list_jobs():
    Job_list = load_jobs_db()
    return jsonify(Job_list)





if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)