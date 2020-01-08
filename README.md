# smogomierz-to-domoticz


## Intro 
Simple script to pull Smog and other metrics from Smogomierz to Domoticz. 
In this particular case, it's Raspberry driven Domoticz

## Relevant Project websites

https://github.com/hackerspace-silesia/Smogomierz

https://www.domoticz.com/wiki/Raspberry_Pi


## Installation

1. Clone code

```
cd /home/pi
git clone https://github.com/zmielna/smogomierz-to-domoticz.git
```

2. Change IP addresses of Smogomierz and Domoticz

```
vim https://github.com/zmielna/smogomierz-to-domoticz.git
```

3. Create Domoticz Dummy Hardware (Setup/Hardware)


4. Create three Domoticz Virtual Sensor Devices (Setup/Hardware/Create Virtual Sensors)

  * Smogomierz T/H/B (Type General, Subtype Temp + Humidity + Baro)
  * Smogomierz PM2.5 (Type General, Subtype Custom Sensor)
  * Smogomierz PM10  (Type General, Subtype Custom Sensor)

5. Take a note of your devices IDX numbers and adjust `smogomierz-to-domoticz.py` idx values respectively, in lines 11 to 13.

6. Finally add cronjob triggered Python script that will fetch data from Smogomierz and push into Domoticz

Either `crontab -e` for pi user

```
*/5 * * * * /home/pi/smogomierz-to-domoticz/smogomierz-to-domoticz.py | logger
```

or add this as a system cronjob

```
echo "*/5 * * * * root /home/pi/smogomierz-to-domoticz/smogomierz-to-domoticz.py | logger" > /etc/cron.d/smogomierz-to-domoticz

```


## Thanks

Big thanks to @github/bfaliszek and @github/hackerspace-silesia and Domoticz crew for all the hard work they put into their projects.
