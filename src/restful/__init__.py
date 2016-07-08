from flask import Flask
from configuration.config import config
from database.cluster import initRedisCluster
from sqlalchemy import create_engine
from model.models import Base

#Initializes Flask application.
app = Flask(__name__)
app.debug = True
# app.config.from_object(config.get('default'))

#Instantiate a new ORM instance.
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Documents/test.db'

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///tiny.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.

#Initializes the redis cluster.
initRedisCluster()

from restful.tiny_routes import tiny
app.register_blueprint(tiny)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)