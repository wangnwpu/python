#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from urllib.request import urlopen

def testserver_get():
    with urlopen('http://127.0.0.1:5000') as response:
        for line in response:
            line = line.decode('utf-8')
            print(line)


# testserver_get()

def testserver_post():
     with urlopen('http://127.0.0.1:5000', data="Request body".encode(encoding="utf-8")) as response:
        for line in response:
            line = line.decode('utf-8')
            print(line)

testserver_post()