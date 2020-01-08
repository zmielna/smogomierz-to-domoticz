#!/usr/bin/python3
import json, urllib.request, codecs
# -------- change here
# change to your Smogomierz IP address
smogomierzip = '192.168.0.236'

# change to your Domoticz IP address
domoticzurl = '192.168.0.176:8080'
# --------- end of changes

smogomierzurl = 'http://%s/api' % (smogomierzip)
response = urllib.request.urlopen(smogomierzurl)
reader = codecs.getreader("utf-8")
responseDictionary = json.load(reader(response))

domoticzurl_thb   = 'http://%s/json.htm?type=command&param=udevice&idx=66&nvalue=0&svalue=%s;%s;0;%s;0' % (domoticzurl, responseDictionary["temperature"], responseDictionary["humidity"], responseDictionary["pressure"])
domoticzurl_pm25   = 'http://%s/json.htm?type=command&param=udevice&idx=72&nvalue=0&svalue=%s' % (domoticzurl, responseDictionary["pm25"])
domoticzurl_pm10   = 'http://%s/json.htm?type=command&param=udevice&idx=73&nvalue=0&svalue=%s' % (domoticzurl, responseDictionary["pm10"])

urllib.request.urlopen(domoticzurl_thb)
urllib.request.urlopen(domoticzurl_pm25)
urllib.request.urlopen(domoticzurl_pm10)
