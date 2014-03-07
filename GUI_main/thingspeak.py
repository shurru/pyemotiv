import httplib, urllib
from time import localtime, strftime
# download from http://code.google.com/p/psutil/
# import psutil
import time

def doit(val, val2):
        cpu_pc = val
        mem_avail_mb = val       
        params = urllib.urlencode({'field1': cpu_pc, 'field3': val2,'key':'ZJWC574G3Y45TWB3'})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        
        try:
                conn.request("POST", "/update", params, headers)
                response = conn.getresponse()
                # print cpu_pc
                # print mem_avail_mb
                # print strftime("%a, %d %b %Y %H:%M:%S", localtime())
                # print response.status, response.reason
                data = response.read()
                conn.close()
        except:
                print "connection failed"        

#sleep for 16 seconds (api limit of 15 secs)
if __name__ == "__main__":
        while True:
                args = sys.argv[1:]
                doit(*args)