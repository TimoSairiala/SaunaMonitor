import serial
from time import sleep
import _mysql
import sys
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read( 'saunasettings.cfg' )

serialport = config.get( 'Section1', 'serialport' )
sqlhost = config.get( 'Section1', 'sqlhost' )
sqluser = config.get( 'Section1', 'sqluser' )
sqlpwd = config.get( 'Section1', 'sqlpwd' )
sqldb = config.get( 'Section1', 'sqldb' )

port = serial.Serial( serialport, 57600, timeout=0.5)
sqlconn = None

try:
	sqlconn = _mysql.connect( sqlhost, sqluser, sqlpwd, sqldb )
	sqlconn.query( "SELECT VERSION()" )
	result = sqlconn.use_result()
	print "MySql version is: %s " % result.fetch_row()[0]
except _mysql.Error, e:
	print "Error %d: %s" % (e.args[0], e.args[1])

while True:
	data = port.read(9999)
	if len(data) > 0:
		print "tallasta: ", data

	sleep( 1 )

port.close()

if sqlconn:
	sqlconn.close()
