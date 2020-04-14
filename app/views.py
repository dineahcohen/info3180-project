"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from app.forms import UserForm
from app.models import UserProfile
import datetime

###
# Routing for your application.
###
@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profile', methods=['GET','POST'])
def addProfile():
    form= UserForm()
    if request.method == "POST":
        if form.validate_on_submit() == True:
            #Gets the user input from the form
            fname = form.firstname.data
            lname = form.lastname.data
            gender = form.gender.data
            email = form.email.data
            location = form.location.data
            bio = form.bio.data
            date = format_date_joined()
            filename = assignPath(form.profile_picture.data)
            
            #create user object and add to database
            user = UserProfile(fname,lname,gender,email,location,bio, date, filename)
            db.session.add(user)
            db.session.commit()

            # remember to flash a message to the user
            flash('User information submitted successfully.', 'success')
        else:
            flash('User information not submitted', 'danger')
        return redirect(url_for("profiles"))  # they should be redirected to a secure-page route instead
    return render_template("addprofile.html", form=form)

#Format date for profile
def format_date_joined():
    now = datetime.datetime.now() #current date
    ## Format the date to return only month and year date
    return now.strftime("%B %d, %Y")

#Save the uploaded photo to a folder
def assignPath(upload):
    filename = secure_filename(upload.filename)
    upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return filename

@app.route("/profiles")
def profiles():
    user_profiles = db.session.query(UserProfile).all()
    return render_template("profilelist.html", users=user_profiles)

@app.route("/profile/<userid>")
def profileId(userid):
    user = db.session.query(UserProfile).filter_by(id=int(userid)).first()
    return render_template("individual.html", user=user)

# The functions below should be applicable to all Flask apps.
# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")