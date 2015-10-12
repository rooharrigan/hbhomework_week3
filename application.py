from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)
app.secret_key = "psh you don't know me"

print "The app is running in the console."

@app.route("/")
def show_index_page():
    """Shows the hoempage form for the job application."""

    return render_template("application-form.html")


@app.route('/favicon.ico')
def favicon():
    """Creates a favicon for the title tab."""

    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'lightning_favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/application-form", methods=['POST'])
def show_form_submission_details():
    """Shows summary page with sheep image after the form is submitted."""

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    jobtype = request.form.get("jobtype")
    unformatted_salary = request.form.get("salary")
    salary = "${:,.2f}".format(int(unformatted_salary))

    return render_template("application-response.html", fname=fname, lname=lname, jobtype=jobtype, salary=salary)



if __name__ == "__main__":
    app.run(debug=True)



# , fname=fname, 
#     lname=lname, jobtype=jobtype, salary=salary