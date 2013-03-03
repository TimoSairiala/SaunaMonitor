import serial
from time import sleep
import _mysql
import sys
import ConfigParser

def is_number( s ):
	try:
		float( s )
		return True
	except ValueError:
		return False

def write_to_sql( humidity, temp ):
#	print "writing to sql"
#	print "insert into temp: %s" % temp
#	print "..and humidity: %s" % humidity
	query = "INSERT INTO mittaukset (heat, humidity) VALUES (%s, %s)" %(temp, humidity)
	print query
	try:
		sqlconn.query( query )
	except _mysql.Error, e:
		print "Error %d: %s" %(e.args[0], e.args[1])

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
#	sqlconn.query( "SELECT VERSION()" )
#	result = sqlconn.use_result()
#	print "MySql version is: %s " % result.fetch_row()[0]
except _mysql.Error, e:
	print "Error %d: %s" % (e.args[0], e.args[1])

while True:
	data = port.read(9999)
	if len(data) > 0:
		print "received: ", data

	# lets see if we received enough sensible data
	# it should be like
	# 'humidity:', '25.50', 'prot\tTemperature', '22.90', 'C'
	measurements = data.split( " " );
#	print measurements
	if measurements[0] == 'Humidity:':
		if measurements[2] == 'pros\tTemperature:':
			if is_number( measurements[1] ):
				if is_number( measurements[3] ):
#					print "humidity is:    %s" % measurements[1]
#					print "temperature is: %s" % measurements[3]
					write_to_sql( measurements[1], measurements[3] )
	
	sleep( 1 )

port.close()

if sqlconn:
	sqlconn.close()
