from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'TzcIy6fr8UlL7DouvbdCHn2gmGq5YePihSJQBOxN'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chet.db'
db = SQLAlchemy(app)

from chetachi import routes