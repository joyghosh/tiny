'''
Created on 02-Jul-2016

Restful API routes to access tiny url shortener as a service.
This architecture makes more sense as it allows to setup tiny as 
an  in-house url shortener service accessible in a distributed network. 

@author: Joy Ghosh
@version:  1.0
@since:  1.0
'''

from flask import Flask
from flask.globals import request

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to tiny.\n \'tiny\' is a scalable and light-weight URL shortener service'

@app.route('/tiny/short',methods=['POST'])
def shorten_url():
    long_url = request.form['url']
    return long_url

@app.route('/tiny/<short_url>', methods=['GET'])
def get_long_url(short_url):
    return short_url

if __name__ == '__main__':
    app.run(debug=True)