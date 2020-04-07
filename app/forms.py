from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField,  SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Length, Email, DataRequired
from flask_wtf.file import FileField, FileRequired, FileField, FileAllowed
from werkzeug.utils import secure_filename

class UserForm(FlaskForm):
    firstname = StringField('First Name', validators=[InputRequired(), Length(max=30)])
    lastname = StringField('Last Name', validators=[InputRequired(), Length(max=30)])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[InputRequired()])
    email = EmailField('Email', validators=[Email(), InputRequired(), Length(max=40)])
    location = StringField('Location', validators=[InputRequired(), Length(max=40)])
    bio = TextAreaField('Biography', validators=[DataRequired(), Length(max=150)])
    profile_picture = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'], 'Only images allowed!')])
    submit= SubmitField('Add Profile')