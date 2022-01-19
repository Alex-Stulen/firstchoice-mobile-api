# Get all shifts by special status for special hospital
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/shift/<int:facility_id>/get-all-by-status?status=...'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
allowed statuses = ['pending', 'certified', 'rejected']
get_fields = {
	'status': <type: str. Required>
	}
	
returns = 'returns array with shift objects. Can be empty'
