# Verification screen

def Verification():

	api_url = 'https://firstchoicenurses.com/api/v1/mobile/auth/verification/'

	method = 'POST'
	headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH

	post_fields = {
		'employee_id': 'employee id field', # required
		'last_four_ssn': 'last four ssn id numbers' # required
	}

	"""
	Note:
		Key Token = None for python or null for JS if authorization is failed
		if authorization is failed: response status = 200 and response will have info about field which field was wrong.
	
		Key role, nurse and facility = null if authorization is failed.
		if role equal 'facility' -> field 'nurse' equal null.
		if role equal 'nurse' -> field 'facility' equal null.
	"""

	returns = {
		'Token': '...', # Authorization Token
		'verified': 'boolean field', # True - if verification is successful. False - if verification is not successful.
		'role': 'nurse or facility. equal null if authorization is failed',
		'nurse': {
			'pk': 'primary key for nurse',
			'is_active_nurse': 'boolean field'
		},
		'facility': {
			'pk': 'primary key for facility'
		},
        'employee_id_is_valid': 'boolean field',
        'last_four_ssn_is_valid': 'boolean field',
	}
