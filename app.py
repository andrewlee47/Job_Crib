from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = 'static'

JOBS = [

    {
        "ID": 1,
        "TITLE": "Virtual Assistance",
        "LOCATION": "Texas",
        "WAGES": "$30/hr"
    },

    {
        "ID": 2,
        "TITLE": "Data analyst",
        "LOCATION": "Dallas",
        "WAGES": "$40/hr"
    },
    {
        "ID": 3,
        "TITLE": "Book keeping",
        "LOCATION": "California",
        "WAGES": "$30/hr"
    },
    {
        "ID": 4,
        "TITLE": "Virtual Nurse",
        "LOCATION": "Chicago",
        "WAGES": "$50/hr"
    }
]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)





if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)