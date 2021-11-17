# Nurse submit shift

def NurseSubmitShift():

	api_url = 'https://firstchoicenurses.com/api/v1/mobile/obj/shift/<int:pk>/submit-by-nurse' # <int:pk> - primary key for shift
	method = 'PUT'
	headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
	post_fields = {
			'some fields for update shift fields. Like in Shift Update ability'
		} 

	returns = {
		'shift data. Read `get_shift.py`'
	}

