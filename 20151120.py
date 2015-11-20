# -*- coding: utf-8 -*- 

##################################################
# 기상청
# http://www.kma.go.kr/weather/lifenindustry/sevice_rss.jsp
# RSS : 웹사이트 상의 컨텐츠를 요약하고 상호 공유할 수 있도록 만든 표준 XML을 기
초로 만들어진 데이터 형식
# RSS 인천 용현동1,4
# http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2817055500

# lxml library 설치해야함
# yum install python-lxml
##################################################
import sys
import json
import requests
import urllib2 # extensible library for opening URLs
import time

from lxml.html import parse, fromstring # processing XML and HTML

# 인천 남구 용현동 기상상황 확인 url
url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2823759100'
url_local ="http://127.0.0.1:4242/api/put"
temp=[]

def insert(metric_name, tag_site, value):
    data={
        "metric":metric_name,
        "timestamp":time.time(),
        "value":value,
        "tags":{
            "site":tag_site
        }
    }
    ret = requests.post(url_local, data=json.dumps(data))
    time.sleep(1)



def temp_process(xml):
        for  elt in xml.getiterator("temp"):    # getting temp tag 
                temp_val = elt.text
                print temp_val

        insert('temperature', 'inchon', temp_val)
        insert('temperature', 'seuol', 20)


if __name__ == '__main__':
    while 1 :
        t = time.localtime()
        tsec = t.tm_sec

        if tsec%10!=0:
                time.sleep(1)
        else :
                page = urllib2.urlopen(url).read()
                print page
                xml_raw = fromstring(page)
                temp_process(xml_raw)
                                                              61,3-17       Bot
