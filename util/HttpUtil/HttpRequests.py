#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

rep = requests.get('http://localhost:5000')
print(rep.text)