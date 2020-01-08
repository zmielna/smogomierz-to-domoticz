# smogomierz-to-domoticz


1. Clone code
2. Change IP addresses of Smogomierz and Domoticz
3. Create Domoticz Dummy Hardware
4. Create three Domoticz Virtual Sensor Devices
 * Smogomierz T/H/B (Type General, Subtype Temp + Humidity + Baro)
 * Smogomierz PM2.5 (Type General, Subtype Custom Sensor)
 * Smogomierz PM10  (Type General, Subtype Custom Sensor)

Take a note of your devices IDX numbers and adjust `smogomierz-to-domoticz.py` code respectively

5. Add cronjob 


```
*/5 * * * * /home/pi/smogomierz-to-domoticz/smogomierz-to-domoticz.py | logger
```

