# Set special shift as certified
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/shift/<int:shift_id>/set-as-certified'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields = {
	'is_certified': <type: bool. Required. Can only be equal as true>
	}
	
returns = {
		'status': 'ok'
	}
	
or returns if request is BAD = {
				'detail': <detail info about error>,
				'status': 'fail'
				}
