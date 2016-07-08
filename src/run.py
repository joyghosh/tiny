'''
Created on 08-Jul-2016

@author: Joy Ghosh
@version:  1.0
'''
from restful import app

if __name__ == '__main__':
    app.logger.debug("Bootstrapping tiny url shortening service.")
    app.run(debug=True)