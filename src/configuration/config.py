'''
Created on 05-Jul-2016

@author: Joy Ghosh
'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))

#Database configuration.
#Possible values ['postgres', 'mysql', 'oracle']
DATABASE = {
    'drivername': os.environ.get('DATABASE_DRIVER') or 'sqlite',
    'host': os.environ.get('DATABASE_HOST'),
    'port': os.environ.get('DATABASE_PORT'),
    'username': os.environ.get('DATABASE_USERNAME'),
    'password': os.environ.get('DATABASE_PASSWORD'),
    'database': os.environ.get('DATABASE_NAME') or 'tiny.db'
}
 
#Redis configuration
REDIS = {
    'url': os.environ.get('REDIS_URL') or 'localhost',
    'port': os.environ.get('REDIS_PORT') or 6379
}        

#Server configuration.
SERVER = {
    'url':os.environ.get('SERVER_URL') or 'localhost'
} 

#mode
DEBUG = True

#Server address
SERVER_ADDRESS = 'localhost'

"""
Application configuration class.
"""
class Config:
    SQLAlchemy_COMMIT_ON_TEARDOWN = True
    
    @staticmethod
    def init_app(app):
        pass
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
                    
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
                        
config = {
            'development': DevelopmentConfig,
            'testing': TestConfig,
            'production': ProductionConfig,
            'default': DevelopmentConfig
          }                                