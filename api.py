# Mobile API

# Note:
# all responses will be serialized to the JSON format

site_url = 'https://firstchoicenurses.com'
dev_site_url = 'https://dev.firstchoicenurses.com'
api_url = '/api/v1/mobile/'
example_api_url = 'https://firstchoicenurses.com/api/v1/mobile/.../'

RETURN_STATUSES = {
	'200': 'ok',
	'201': 'Created',
	'401': 'Unauthorized',
	'403': 'Forbidden',
	'404': 'Not Found',
	'405': 'Method Not Allowed',
	'500': 'Internal Server Error',
}

# Each request must contain headers with an Authorization key and a Token
REQUIRED_HEADERS_FOR_TOKEN_AUTH = {
	'Authorization': 'Token 123123123',
	# Key: Authorization - required.
	# Word 'Token' in Value - required.
	# One space after 'Token' - required.
	# Only one space in Value - required.
}


"""	
	Response Status.

	Returns status 401 Unauthorized:
	 IF  Invalid token. 
	 OR  Authentication credentials were not provided. -> Perhaps the Authorization key in headers is missing.
	 OR  the user has not passed verification or authorization.
	 
	 fields that were invalid will be returned with a boolean operator. For example: {'employee_id_is_valid': False}.
	 erroneous field will be sent as field name and prefix at the end: {'<field_name>_is_valid': False or True}.
"""

"""
	Authorization.

	Key Token in response equal `None` for python or `null` for JS if user authorization is failed. 

"""