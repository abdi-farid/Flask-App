from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jhgvdsjhgvkhgvsfdkjhblkjb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# db will be used in other files
# It's a SQLAlchemy instance taking current file name in parameter
db = SQLAlchemy(app)
# in terminal db.create_all() to create database 

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
