# (for facility admin) Nurse assign to shift
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/nurse/<int:nurse_id>/assign-to-shift'
method = 'PUT'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
put_fields = {
	"shift_id": <type: integer. Required>
	}

returns = 'assigned shift object'
