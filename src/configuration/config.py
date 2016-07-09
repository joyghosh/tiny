'''
Created on 05-Jul-2016

@author: Joy Ghosh
'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))

#Database configuration.
DATABASE_ENGINE = 'postgresql'            #Possible values ['postgresql', 'mysql', 'oracle']
DATABASE_USERNAME = ''
DATABASE_PASSWORD = ''
 
#Redis configuration
REDIS_URL = 'localhost'
REDIS_PORT = 6379
 
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