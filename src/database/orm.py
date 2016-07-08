'''
Created on 05-Jul-2016

Object relational mapper. 
A Gateway for all CRUD operations on url mapping resource. 

@author: Joy Ghosh
@version:  1.0
@since:  1.0
'''

from sqlalchemy.orm import sessionmaker
# engine = create_engine('sqlite:///tiny.db')
# Base.metadata.bind = engine

def createOrUpdate(urlmap):
    
    from restful import engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    
    obj = get(urlmap.uuid, urlmap.short_url) 
    if(obj == None):
        session.add(urlmap)
        session.commit()
        obj = urlmap
    
    print obj
    return obj

def delete(urlmap):
    from restful import engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    
    session.delete(urlmap)
    session.commit()

def get(uuid, short_url):
    
    from restful import engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    
    from model.models import UrlMapping
    result = session.query(UrlMapping).filter(UrlMapping.short_url == short_url).first()
    print result
    
    if(not result == None):
        return result.url
    else:
        return None