'''
Created on 02-Jul-2016

@author: Joy Ghosh
@version: 1.0
@since: 1.0
'''
from flask_sqlalchemy import SQLAlchemy
from restful.tiny_routes import app

db = SQLAlchemy(app)

class UrlMap(db.Model):
    '''
    A model responsible for storing shortened to long url mapping.
    '''
    id = db.Column('id', db.Integer, primary_key = True)
    uuid = db.Column('uuid', db.Integer, unique = True)
    short_url = db.Column('short_url', db.String(255), unique = True)
    url = db.Column('url', db.String(255), unique = True)
    
    def __init__(self, uuid, short_url, url):
        '''
        Constructor
        '''
        self.uuid = uuid
        self.short_url = short_url
        self.url = url
        