# Nurse get all booked shifts
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/all-booked-shifts'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed' 

returns = [
			{'shift object. Read `get_shift.py`'},
			...,
			...,
			{'shift object. Read `get_shift.py`'}
		]