import os

from flask import Flask

from application.databaseFunctions import insert_base_colours
from application.database import db

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'cars.db')


@app.before_first_request
def create_database() :
    db.init_app(app)
    db.create_all()
    insert_base_colours()


from application import routes

