#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import urllib
from urllib import parse
from urllib.request import urlopen
import requests
import json


# urllib
# http get
def http_get_urllib(url, header, params):
    querystring = parse.urlencode(params)

    requ = urllib.request.Request(url + '?' + querystring, None,headers=header)
    resp = urllib.request.urlopen(requ)

    body = resp.read()
    head = resp.info()

    respstr = dict(httpheader=str(head), httpbody=body.decode('utf-8'))
    resp_json = json.dumps(respstr, ensure_ascii=False)

    return resp_json


# http post
def http_post_urllib(url, header, params):
    data = parse.urlencode(params).encode('utf-8')

    requ = urllib.request.Request(url, data, header)
    resp = urllib.request.urlopen(requ)

    body = resp.read()
    head = resp.info()

    respstr = dict(httpheader=str(head), httpbody=body.decode('utf-8'))
    resp_json = json.dumps(respstr, ensure_ascii=False)

    return resp_json


# test: http_get_urllib(url, header, params)
def test_urllib():
    header = {
        'user-agent' : 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)',
        'connection' : 'Keep-Alive'
    }

    param = {
        'tn' : 'monline_3_dg',
        'ie' : 'utf-8',
        'wd' : '因特网'
    }

    url = 'http://localhost:5000'

    print('http get result: ' + http_get_urllib(url, header, param))
    print('http get result: ' + http_post_urllib(url, header, param))

# test_urllib()


# requests
# http get
def http_get_requests(url, header, params):
    resp = requests.get(url, params=params, headers=header)

    respstr = dict(httpbody=resp.text, httpheader=str(resp.headers))
    resp_json = json.dumps(respstr, ensure_ascii=False)

    return str(resp_json)


# http post
def http_post_requests(url, header, params):
    resp = requests.post(url, data=params, headers=header)

    respstr = dict(httpbody=resp.text, httpheader=str(resp.headers))

    resp_json = json.dumps(respstr, ensure_ascii=False)

    return str(resp_json)


# test: http_get_requests(url, header, params)
def test_requests():
    header = {
        'user-agent' : 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)',
        'connection' : 'Keep-Alive'
    }
    param = {
        'tn' : 'monline_3_dg',
        'ie' : 'utf-8',
        'wd' : '因特网'
    }

    resp = http_get_requests('http://localhost:5000', header, param)
    print('http get result: ' + resp)
    resp = http_post_requests('http://localhost:5000', header, param)
    print('http post result: ' + resp)


# test_requests()
