from flask import Flask
from flask_sqlalchemy import SQLAlchemy
    
# Create the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'
app.config['SECRET_KEY'] = '42846b27ed0d5a71e21f132d86aa3ad6ca6fb803fc32b080a1ca596186e0679d'

# Create database instance
db = SQLAlchemy(app)

from app import routes