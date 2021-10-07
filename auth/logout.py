# Logout ability

def Logout():
	api_url = 'https://firstchoicenurses.com/api/v1/mobile/auth/logout'

	method = 'GET'
	headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH

	get_fields = 'special get fields are not needed'

	# Note:
	#	if logout is success:
	#		returns status code 200.
	#	else:
	#		returns status code 401.
	#
	# special data in response missing
	returns = {}

