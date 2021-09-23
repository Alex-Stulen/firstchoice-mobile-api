# Login screen

def Login():

	api_url = 'https://firstchoicenurses.com/api/v1/mobile/auth/login/'

	method = 'POST'
	headers = 'special headers are not needed'

	post_fields = {
		'email': 'email field', # required
		'password': 'password field' # required
	}

	"""
	Note:
		Key Token = None for python or null for JS if authorization is failed.
		if authorization is failed: 
			response status = 200 and response will have info about field which field was wrong.
			key user equal null.

		if user['role'] is facility you must redirect to app without verification page.

	"""
	returns = {
		'Token': '...', # Authorization Token
		'authorized': 'boolean field', # True - if authorization is successful. False - if authorization is not successful
		'user': {
			'pk': 'primary key for nurse or facility',
			'role': 'nurse or facility',
		}
  		'email_is_valid': 'boolean field',
  		'password_is_valid': 'boolean field'
	}
