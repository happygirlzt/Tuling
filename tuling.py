#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

x = 1
while x: 
	KEY = '92ec002f44bf44bfb7fda1060faeb057'
	url = 'http://www.tuling123.com/openapi/api'

	req_info = raw_input()
 
	query = {'key': KEY, 'info': req_info}
	headers = {'Content-type': 'text/html', 'charset': 'utf-8'}
 
# 用requests模块以get方式获取内容
	r = requests.get(url, params = query, headers = headers)
	st = r.text[23:-2]
	print st