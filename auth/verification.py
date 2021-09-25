# Verification screen
# this screen unavailable for facility. 

def Verification():

	api_url = 'https://firstchoicenurses.com/api/v1/mobile/auth/verification/'

	method = 'POST'
	headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH

	post_fields = {
		'pk': '<type: int> pk - the primary key of the user (nurse) to be verified',
		'employee_id': 'employee id field', # required
		'last_four_ssn': 'last four ssn id numbers' # required
	}

	"""
	Note:
		Key Token = None for python or null for JS if authorization is failed
		if authorization is failed: response status = 200 and response will have info about field which field was wrong.
	
		Key user = null if authorization is failed.
		
		verification page only for nurse.
	"""

	returns = {
		'Token': '...', # Authorization Token
		'verified': 'boolean field', # True - if verification is successful. False - if verification is not successful.
		'user': {
			'pk': 'primary key for nurse',
			'role': 'nurse',
			'is_active_user': 'boolean field'
		},
        'employee_id_is_valid': 'boolean field',
        'last_four_ssn_is_valid': 'boolean field',
	}
