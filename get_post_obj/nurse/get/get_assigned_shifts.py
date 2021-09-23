# Get assigned nurse shifts


def Get_Assigned_Shifts():

	"""
		Note:
			to get assigned shift, you do not need to specify the fields for a get request. 
			It is enough to specify the primary key of the nurse in the address bar instead of <pk>.
	"""
	api_url = 'https://firstchoicenurses.com/api/v1/mobile/obj/nurse/<pk>/assigned-shifts/'

	method = 'GET'
	headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH

	get_fields = 'special get fields are not needed'

	# key assigned_shifts is array which contain object with 'key -> value' structure.
	# if shifts is not found -> assigned_shifts length equal 0. 
	returns = {
		'assigned_shifts': [
			{'pk': 'primary key for shift'},
			...,
			...,
			{'pk': 'primary key for shift'}
		]
	}
