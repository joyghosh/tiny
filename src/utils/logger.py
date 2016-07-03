'''
Created on 03-Jul-2016

@author: Joy Ghosh
@version:  1.0
@since:  1.0
'''

from restful.tiny_routes import app

def getLogger():
    logger = app.logger()
    logger.debug("returning logger object.")
    return logger