import ConfigParser

config = ConfigParser.RawConfigParser()
config.add_section( 'Section1' )

serialport = raw_input( "Enter serialport to be used: " )
sqlhost = raw_input( "MySql server address: " )
sqluser = raw_input( "MySql username: " )
sqlpwd = raw_input( "MySql password: " )
sqldb = raw_input( "MySql database: " )

config.set( 'Section1', 'serialport', serialport )
config.set( 'Section1', 'sqlhost', sqlhost )
config.set( 'Section1', 'sqluser', sqluser )
config.set( 'Section1', 'sqlpwd', sqlpwd )
config.set( 'Section1', 'sqldb', sqldb )

with open( 'saunasettings.cfg', 'wb' ) as configfile:
	config.write( configfile )

