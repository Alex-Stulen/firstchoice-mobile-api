# Nurse assign to shift

def AssignToShift():

	api_url = 'https://firstchoicenurses.com/api/v1/mobile/obj/nurse/assign-to-shift'
	method = 'POST'
	headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
	post_fields = {
			"shift_id" <type: integer or string>
		} 

	returns = {
			'assign_shift': {...}
		}

