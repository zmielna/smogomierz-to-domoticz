#!/usr/bin/python3
import json, urllib.request, codecs

smogomierzurl = 'http://192.168.0.236/api'
response = urllib.request.urlopen(smogomierzurl)
reader = codecs.getreader("utf-8")
responseDictionary = json.load(reader(response))
#print(responseDictionary.values())
#print(responseDictionary.keys())
#print(responseDictionary)
domoticzurl_thb   = 'http://192.168.0.176:8080/json.htm?type=command&param=udevice&idx=66&nvalue=0&svalue=%s;%s;0;%s;0' % (responseDictionary["temperature"], responseDictionary["humidity"], responseDictionary["pressure"])
#print(domoticzurl_thb)
urllib.request.urlopen(domoticzurl_thb)
