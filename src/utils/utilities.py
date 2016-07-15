'''
Created on 03-Jul-2016

@author: Joy Ghosh.
@version: 1.0.
@since: 1.0.
'''

import urllib2
# from logger import getLogger

'''
Determines if it is a valid url.
'''
def validate_url(url):
#     logger = getLogger()
#     logger.debug("validating the url......")
    try:
        urllib2.urlopen(url, timeout=10)
    except urllib2.HTTPError, e:
#         logger.error(e)
        return False
    except urllib2.URLError, e:
#         logger.error(e)
        return False
    
    return True

'''
Utility method to from 
'''
def db_connection_string(db_vendor, username, passwd):
    pass