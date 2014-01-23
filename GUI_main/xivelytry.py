import xively
import datetime
import sys
import time
import xml.etree.ElementTree as etree
import numpy

XIVELY_API_KEY= "OXrsK9MwFkcLIJvMRlAouni0TBSYPbT2ZU3tuPpP2uqTZfxi"
XIVELY_FEED_ID= 146826075

def updata(val):
    api = xively.XivelyAPIClient(XIVELY_API_KEY)
    feed = api.feeds.get(XIVELY_FEED_ID)
    now = datetime.datetime.utcnow()
    # tmpr=[]
    
    # watts=[]
    # for i in xrange(0,20): 
    # 	tmpr.append(numpy.random.randint(20,50))
    # 	watts.append(numpy.random.randint(0,5000))
         
    feed.datastreams = [
	    xively.Datastream(id='tmpr', current_value=val, at=now),
	    xively.Datastream(id='watts', current_value=val, at=now),
	]
    feed.update()
    
  
    
if __name__ == '__updata__':
    try:
        args = sys.argv[1:]
        main(*args)
    except KeyboardInterrupt:
        pass