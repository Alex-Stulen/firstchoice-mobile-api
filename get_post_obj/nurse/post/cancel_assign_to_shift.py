# Nurse Cancel assign to shift

def CancelAssignToShift():

	api_url = 'https://firstchoicenurses.com/api/v1/mobile/obj/nurse/cancel-assign-to-shift'
	method = 'POST'
	headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
	post_fields = {
			"shift_id" <type: integer or string>
		} 

	returns = 'no content'

