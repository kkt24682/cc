#!/usr/bin/python

import sys
import urllib2
import time
import json
import requests
from datetime import datetime, timedelta
count = 2015
while 1 :
        t = time.localtime()
        tsec = t.tm_sec
        if tsec%10!=0 :
                print tsec
                time.sleep(0.2)
                count=count+200
        else :
                url = "http://127.0.0.1:4242/api/put"
                data =  {
                "metric": "foo.bar",
                "timestamp": time.time(),
                "value": 2015+count,
                "tags":
                {
                "host": "mypc"
                }
                        }

                ret = requests.post(url, data=json.dumps(data))
                print "ok"
