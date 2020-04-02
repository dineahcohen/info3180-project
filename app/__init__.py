from flask import Flask
 
app = Flask(__name__)
app.config['SECRET_KEY'] = "$up3rDup3R3K3Y"
from app import views