# Verification screen

def Verification():

	api_url = 'https://firstchoicenurses.com/api/v1/mobile/auth/verification/'

	method = 'POST'
	headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH

	post_fields = {
		'employee_id': 'employee id field', # required
		'last_four_ssn': 'last four ssn id numbers' # required
	}

	# Note:
	# Key Token = None for python or null for JS if authorization is failed
	returns = {
		'Token': '...', # Authorization Token
		'verified': 'boolean field', # True - if verification is successful. 
									 # False - if verification is not successful.
        'employee_id_is_valid': 'boolean field',
        'last_four_ssn_is_valid': 'boolean field',
	}
