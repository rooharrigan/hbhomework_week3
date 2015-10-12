from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "psh you don't know me"

print "The app is running in the console."

@app.route("/")
def show_index_page():
    """Shows the form."""

    print "You're in the home route"
    return render_template("application-form.html")


@app.route("/application-form", methods=['POST'])
def show_form_submission_details():
    """Shows completion message after the form is submitted."""

    print "You're in the application-form route"
    print request
    print request.form
    print type(request)
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    jobtype = request.form.get("jobtype")
    unformatted_salary = request.form.get("salary")
    salary = "${:,.2f}".format(int(unformatted_salary))

    flash("Sheep is happy you applied.")

    return render_template("application-response.html", fname=fname, lname=lname, jobtype=jobtype, salary=salary)



if __name__ == "__main__":
    app.run(debug=True)



# , fname=fname, 
#     lname=lname, jobtype=jobtype, salary=salary