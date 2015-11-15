# MarcoPoli
Marco Poli is a system composed by a network of sensors placed around Politecnico which send information about temperature, noise, congestion, humidity and light to a server. These informations are elaborated and a thematic map is created where critical zones and events are marked.

The students can decide to log-in or not. If the student doesn’t log-in, he can just watch the map with the critical zones on it, together with some other (limited) services. Otherwise, by logging in, he can setup favourite parameters such as zones inside Politecnico, temperature, noise, congestion level, humidity and light level. A list of possible destinations is generated and shown to the user according to the configuration chosen.

The system is not a “navigation” system because doesn’t tell the user how to reach a zone inside Politecnico. A selected user (administration, owner of a bar, etc.) can add a place of interest visible to all the other students that are using the app in another thematic map.

## Server

## Station
Components:
- Raspberry Pi (B+ or 2)
- 2A Battery or wall-adapter
- Pi camera Rev 1.3
- Razberry
- Z-Wave Multiple sensor
- USB Microphone
- Wifi module (or LAN cable)

## Station-Server protocol
\<server-ip\>/newstation, POST
	header: application/json
	body:	Json file

		station_id:	<station-id>
		lat:		<latitude>
		lon:		<longitude>

	response: Json file
		
		state: True/False -> True: 	Start the station (the station will start sending data to the server)
				     False:	Do not start the station (the station will not start sending data)
		
		sleep: <seconds>  -> If ‘state’ = False, the station will send another newstation request in <seconds> seconds (integer)

		msg: <text>

	ATTENTION: If response state = False, the station will send another POST request to the server after a sleep time


\<server-ip\>/stations/<station-id>, POST
	header:	application/json
	body:	Json file
		
		temperature:	<temperature>
		humidity:	<humidity>
		light:		<light>
		noise:		<noise level>	-> scale from 0 to 10 (scale may change!)
		people:		<people>	-> congestion scale from 0 to 10 (scale may change!)

	response: Json file
		
		state: True/False -> True: 	Continue sending data
				     False:	Stop sending data

		sleep: <seconds>  -> If ‘state’ = False, the station will send a /restart request after <seconds> seconds

		msg: <text>

\<server-ip\>/stations/\<station-id\>/restart, GET
	header: NONE
	body:	NONE

	response: Json file
		
		state: True/False -> True: 	Restart sending data
				     False:	Do no send data

		sleep: <seconds>  -> If ‘state’ = False, the station will send another /restart request after <seconds> seconds

		msg: <text>

