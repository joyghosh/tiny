'''
Created on 02-Jul-2016

This module contains the forward and backward mapping functions
needed to shorten a given url. As opposed to url-value based hash mechanism, 
we are using a counter based hash approach where a universally unique counter
value is hashed to a short string of characters. This becomes the new shortened 
url and the key for the (key->value) pair where shortened url is the key and 
value is the actual or (assumed) long url. e.g. ('Bsh1'->'www.example.com').

Feature set is as follows:
(1) Generates a shortened url using a long integer value.
(2) Retrieves the long integral value from a short url. 

@author: Joy Ghosh
@version:  1.0
@since:  1.0
'''
from database.cluster import get_current_uuid

#Sequence of possible characters in a url.
charset = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
           'w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
           'S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9'];

#charset size
CHARSET_SIZE = 62

#converts an numeric id to short url.
def to_short_url(long_url):
    
    from model.models import UrlMapping
    short_url = ""
    uuid = get_current_uuid()
    while uuid:
        short_url = charset[uuid % CHARSET_SIZE] + short_url
        uuid = (uuid/CHARSET_SIZE)
    
    urlmap = UrlMapping(uuid, short_url, long_url)
    urlmap.save()

    #return the shorter version.
    return short_url

#converts from short url to numeric id.
def to_long_url(short_url):
    
    from model.models import UrlMapping
    
    uuid = 0
    for i in range(0, len(short_url)):    
        if(ord('a') <= ord(short_url[i]) and ord(short_url[i]) <= ord('z')):
            uuid = ((uuid * CHARSET_SIZE) + ord(short_url[i]) - ord('a'))
        elif(ord('A') <= ord(short_url[i]) and ord(short_url[i]) <= ord('Z')):
            uuid = ((uuid * CHARSET_SIZE) + ord(short_url[i]) - ord('A') + 26)
        elif(ord('0') <= ord(short_url[i]) and ord(short_url[i]) <= ord('9')):
            uuid = ((uuid * CHARSET_SIZE) + ord(short_url[i]) - ord('0') + 52)
    
    return UrlMapping.fetch(uuid, short_url)