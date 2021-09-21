# Login screen

def Login():

	api_url = 'https://firstchoicenurses.com/api/v1/mobile/auth/login/'

	method = 'POST'
	headers = 'special headers are not needed'

	post_fields = {
		'email': 'email field', # required
		'password': 'password field' # required
	}

	# Note:
	# Key Token = None for python or null for JS if authorization is failed
	returns = {
		'Token': '...', # Authorization Token
		'authorized': 'boolean field', # True - if authorization is successful. False - if authorization is not successful
  		'email_is_valid': 'boolean field',
  		'password_is_valid': 'boolean field'
	}
