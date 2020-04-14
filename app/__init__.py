from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "$up3rDup3R3K3Y"
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://rjzbqcvepeliow:f9ccc4d76bb5ba1d50bbb268cf2649da7784b01f334bba9f88590de6a1097058@ec2-34-197-212-240.compute-1.amazonaws.com:5432/d2c6fvcffkoc5u'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
app.config['UPLOAD_FOLDER'] = './app/static/uploads'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views

