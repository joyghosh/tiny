'''
Created on 02-Jul-2016
@author: Joy Ghosh
@version:  1.0
@since:  1.0
'''

"""
Restful API routes to access tiny url shortener as a service.
This architecture makes more sense as it allows to setup tiny as 
an  in-house url shortener service accessible in a distributed network. 
"""

from flask import Flask
from flask.globals import request
from database.cluster import initRedisCluster
from mapper.mappers import to_short_url, to_long_url
from utils.utilities import validate_url

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

@app.route('/')
def welcome():
    return 'Welcome to tiny.\n \'tiny\' is a scalable and light-weight URL shortener service'

@app.route('/tiny/short',methods=['POST','GET','HEAD','PUT','DELETE'])
def shorten_url():
    if(request.method == 'POST'):
        long_url = request.form['url']
        
        #determine url validity.
        if(validate_url(long_url)):
            return to_short_url(long_url)
        else:
            return '<h1>Invalid url</h1>' 
    else:
        return '<h1>Method not allowed</h1>', 405

@app.route('/tiny/<short_url>', methods=['GET'])
def get_long_url(short_url):
    return to_long_url(short_url)

if __name__ == '__main__':
    app.logger.debug("Bootstrapping tiny, a url-shortener service.")
    initRedisCluster()
    app.run(debug=True)