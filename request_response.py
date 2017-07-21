#!/usr/bin/env python

import urllib
import base64
import HackerRank
from pprint import pprint


api_key = "hackerrank|2755998-1616|097a96f931a5a0ccfaf8f5416aeff414aef544de"
source = "puts 'Testing'"
lang = 5
testcases = "[\"Test 1\", \"Test 2\"]"
format = "JSON"

try:
	api_client = HackerRank.swagger.ApiClient()
	checker_api = HackerRank.ChekerApi(api_client)
	response = checker_api.languages()
	response2 = checker_api.submission(api_key, source, lang, testcases,\
		format, callback_url="https://testing.com/response/handler", wait="true")
	pprint(response)
	pprint(response2)


except urllib2.HTTPError as e:
	print('[HTTP Error {}]: {}'.format(e.code, e.reason))
	print('REquest URL: {}'.format(e.geturl()))
	print('Response body: {}'.format(e.read()))

except urllib2.URLError as e:
	print('[URL Error]: {}'.format(e.reason))

except Exception as e:
	print(e)
