from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import locale

#Set location for currency formatting
locale.setlocale(locale.LC_ALL, '')


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def serve_homepage():
    """Returns the homepage when users visit the website"""

    return render_template("index.html")


@app.route("/application-form")
def serve_application_form():
    """Displays the application for to the user"""

    job_list = ["Software Engineer", "QA Engineer", "Product Manager"]

    return render_template("application-form.html", job_list=job_list)


@app.route("/application-success", methods=["POST"])
def serve_application_response():
    """Displpays the user's inputs as a response to their post request"""

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    salary = float(request.form.get("salary"))
    job_title = request.form.get("job")

    #Format salary
    salary = locale.currency(salary, grouping=True)

    return render_template("application-response.html", fname=fname, lname=lname,
                           salary=salary, job_title=job_title)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
