# Verification screen

def Verification():

	api_url = 'https://firstchoicenurses.com/api/v1/mobile/auth/verification/'

	method = 'POST'
	headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH

	post_fields = {
		'employee_id': 'employee id field <type: int>', # required
		'last_four_ssn': 'last four ssn id numbers <type: int>' # required
	}

	"""
	Note:
		Key Token = None for python or null for JS if authorization is failed
		if authorization is failed: 
			response status = 401
	"""

	returns = {
		'token': <type: str>,
		'verified': 'boolean field', # True - if verification is successful. False - if verification is not successful.
		'user': {
			'pk': 'primary key for nurse <type: int>',
			'role': 'nurse',
			'is_active_user': '<type: bool>'
		},
        	'employee_id_is_valid': '<type: bool>',
        	'last_four_ssn_is_valid': '<type: bool>',
	}

