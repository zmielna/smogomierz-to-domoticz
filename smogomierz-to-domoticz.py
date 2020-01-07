#!/usr/bin/python3
import json, urllib.request, codecs

smogomierzurl = 'http://192.168.0.236/api'
response = urllib.request.urlopen(smogomierzurl)
reader = codecs.getreader("utf-8")
responseDictionary = json.load(reader(response))
print(responseDictionary)
