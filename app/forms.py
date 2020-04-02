from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Length, Email, DataRequired
from flask_wtf.file import FileField, FileRequired, FileField, FileAllowed
from werkzeug.utils import secure_filename

class UserForm(FlaskForm):
    first_name = StringField('fname', validators=[InputRequired(), Length(max=30)])
    last_name = StringField('lname', validators=[InputRequired(), Length(max=30)])
    gender = SelectField('gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[InputRequired()])
    email = EmailField('email', validators=[Email(), InputRequired(), Length(max=40)])
    location = StringField('location', validators=[InputRequired(), Length(max=40)])
    bio = TextAreaField('bio', validators=[DataRequired(), Length(max=150)])
    profile_picture = FileField('photo', validators=[FileRequired(), FileAllowed(['jpg','png'], 'Only jpg and png files allowed!')])