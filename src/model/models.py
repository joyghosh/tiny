'''
Created on 02-Jul-2016

@author: Joy Ghosh
@version: 1.0
@since: 1.0
'''
import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine 

from database.orm import createOrUpdate, delete, get

Base = declarative_base()

class UrlMapping(Base):
    '''
    A model responsible for storing shortened to long url mapping.
    '''
    #table name
    __tablename__ = 'url_mapping'
    
    #Columns of the table.
    id = Column('id', Integer, primary_key = True, autoincrement=True)
    uuid = Column('uuid', Integer)
    short_url = Column('short_url', String(255), unique = True)
    url = Column('url', String(255))
    createdAt = Column('createdAt', DateTime)
    updatedAt = Column('updatedAt', DateTime)
#
    def __init__(self, uuid, short_url, url):
        '''
        Constructor
        '''
        self.uuid = uuid
        self.short_url = short_url
        self.url = url
        self.createdAt = self.updatedAt = datetime.datetime.now()
    
    def __repr__(self):
        return '<UrlMap %r>' % (self.short_url)
    
    """
    First it check mapping already exists (chances of which are less).
    If yes, it returns the old map or else creates a new one and returns it. 
    """
    def save(self):
        createOrUpdate(self)
     
    def remove(self):
        delete(self)
     
    @staticmethod
    def fetch(uuid, short_url):
        return get(uuid, short_url)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
# engine = create_engine('sqlite:///tiny.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
# Base.metadata.create_all(engine)