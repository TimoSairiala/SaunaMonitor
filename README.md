SaunaMonitor
============

The target of the project is to send temperature
(and maybe some other parameters as well) over ZigBee
network.

There will be three different root directories
- SaunaSender is code for Arduino.
   This should be uploaded for Arduino board that is 
   connected to ZigBee network adapter and temperature
   sensor.

- SaunaReceiver is python code for ZigBee receiver
   You should first configure it by running saunaconfig.py
   and apply mysql and serial port details

- SaunaPlotter does not exist yet
   SaunaPlotter will be fetching measurement details from
   the database and draw (hopefully) nice graphs

