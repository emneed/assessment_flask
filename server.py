from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route("/")
def serve_homepage():
    """Returns the homepage when users visit the website"""
    return render_template("index.html")

@app.route("/application-form")
def serve_application_form():
    """Displays the application for to the user"""
    job_list = ["Software Engineer", "QA Engineer", "Product Manager"]

    return render_template("application-form.html", job_list=job_list)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
