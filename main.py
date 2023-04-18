import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route("/")
def index():
    students = ['Moshe', 'David', 'Yosef', 'Shalom']
    return render_template("index.html", name="ori", address="Jerusalem", students=students)    


app.run(debug=True)