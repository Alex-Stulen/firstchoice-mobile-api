# Login screen

def Login():

	api_url = 'https://firstchoicenurses.com/api/v1/mobile/auth/login'

	method = 'POST'
	headers = 'special headers are not needed'

	post_fields = {
		'email': 'email field', # required
		'password': 'password field' # required
	}

	"""
	Note:
		if authorization is failed: 
			response status = 401
	"""
	returns = {
		'token': '... <type: str>', # Authorization Token
		'authorized': '<type: bool>', # True - if authorization is successful. False - if authorization is not successful
		'user': {
			'pk': 'primary key for nurse or facility <type: int>',
			'role': 'nurse or facility <type: str>',
		}
  		'email_is_valid': '<type: bool>',
  		'password_is_valid': '<type: bool>'
	}

