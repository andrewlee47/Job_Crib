import os.path

from flask import Flask, render_template, jsonify, request

from database import load_jobs_db, job_details_db, text, engine
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.static_folder = 'static'

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def careerbuilder():
    Job_list = load_jobs_db()
    return render_template('home.html', jobs = Job_list)



@app.route("/job/<id>")
def display_job(id):
    job = job_details_db(id)

    if not job:
        return "Not found", 404
    return render_template('jobpage.html', job = job)


@app.route("/job/<id>/apply", methods = ['POST'])
def job_application(id):
    data = request.form
    job = load_jobs_db()

    if 'Resume' in request.files:
        resume_files = request.files['Resume']
        if resume_files.filename != '':
            filename = secure_filename(resume_files.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            resume_files.save(file_path)

    with engine.connect() as conn:
        query = text(
            "INSERT INTO Applications (full_name, email, phone_number, experience, linkedIn, Resumes)"
            " VALUES (:full_name, :email, :phone_number, :experience, :linkedin, :resume_path)")

        conn.execute(query, {
            'full_name': data['full_name'],
            'email': data['email'],
            'phone_number': data['phone_number'],
            'experience': data['Experience'],
            'linkedin': data['LinkedIn'],
            'resume_path': file_path
        })

        conn.commit()

    return render_template('submitted_application.html', application = data, job = job)


@app.route("/api/jobs")
def list_jobs():
    Job_list = load_jobs_db()
    return jsonify(Job_list)


if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)
