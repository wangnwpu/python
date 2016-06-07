#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import urllib
from urllib import parse
from urllib.request import urlopen

# urllib
def httpGet(url, header, params):
    querystring = parse.urlencode(params)
    with urlopen(url + '?' + querystring) as response:
        for line in response:
            line = line.decode('utf-8')
            print(line)

param = {
    'tn' : 'monline_3_dg',
    'ie' : 'utf-8',
    'wd' : '因特网'
}

url = 'http://www.baidu.com/baidu'

# httpGet(url, None, param)







