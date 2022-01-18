# Get current Facility Admin Detail info
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed'

returns = {
	    "id": 83,
	    "username": "testfacility",
	    "first_name": "",
	    "last_name": "",
	    "email": "testfacility@gmail.com",
	    "date_joined": "2022-01-18T15:07:32.779427-05:00"
	}

