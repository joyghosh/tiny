'''
Created on 02-Jul-2016

Mock store.
@author: Joy Ghosh
@version:  1.0
@since:  1.0
'''

#For test purpose only. Mock the url mapping.
mock_cache = {}

def insert(key, value):
    if(not mock_cache.has_key(key)):
        mock_cache[key] = value
    
    return mock_cache[key]

def remove(key):
    if(mock_cache.has_key(key)):
        del mock_cache[key]
        
def get(key):
    return mock_cache[key]        