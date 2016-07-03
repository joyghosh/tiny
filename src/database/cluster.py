'''
Created on 03-Jul-2016

@author: Joy Ghosh
@version:  1.0
@since:  1.0
'''
from redis.exceptions import WatchError

"""
Interaction of tiny with the redis cluster.
"""

#from rediscluster import StrictRedisCluster
import redis
#from utils.logger import getLogger
import time

#logger = getLogger()
REDIS_KEY = "tiny_counter"
REDIS_LOCK = "tiny_lock"

#startup_nodes = [{"host": "127.0.0.1", "port": "6379"}]
#rc = StrictRedisCluster(startup_nodes=startup_nodes,decode_responses=True)
rc = redis.StrictRedis(host='localhost', port=6379, db=0)

"""
Initialize the redis cluster. Following protocol is followed.

(1) Checks if the cluster wide key for unique long value exists. 
    If key exists, no action required.
    
(2) If no key is found acquire a cluster wide distributed lock and
    set the value of the counter.
"""
def initRedisCluster():
    
    #logger.debug("Initializing the redis cluster.")
    if(not rc.exists(REDIS_KEY)):
        value = long(time.time())
        rc.set(REDIS_KEY, value)

"""
Returns the cluster wide unique counter and increments the 
old counter value. 
"""
def get_current_uuid():
     
    #logger.debug("return current value.")
    
    pipe = rc.pipeline(transaction=True)
    
    while True:
        try:
            pipe.watch(REDIS_KEY)
            uuid = long(rc.get(REDIS_KEY))
            pipe.multi()
            pipe.incr(REDIS_KEY)
            pipe.execute()
            break
        except WatchError:
            continue
    
    return uuid
    