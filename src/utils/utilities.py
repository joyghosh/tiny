'''
Created on 03-Jul-2016

@author: Joy Ghosh.
@version: 1.0.
@since: 1.0.
'''

import urllib2

'''
Determines if it is a valid url.
'''
def validate_url(url):
    try:
        urllib2.urlopen(url, timeout=10)
    except urllib2.HTTPError, e:
        return False
    except urllib2.URLError, e:
        return False
    
    return True