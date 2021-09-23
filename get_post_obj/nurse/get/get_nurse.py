# Get detail nurse info


def Get_Nurse():

	"""
		Note:
			to get information about a nurse, you do not need to specify the fields for a get request. 
			It is enough to specify the primary key of the nurse in the address bar instead of <pk>.
	"""

	api_url = 'https://firstchoicenurses.com/api/v1/mobile/obj/nurse/<pk>/'

	method = 'GET'
	headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH

	get_fields = 'special get fields are not needed'

	# if nurse with this pk is not found response will returns status code: 404 Not Found.
	returns = {
		'nurse': {
			'pk': 'primary key for nurse',
			'role': 'nurse',
			'email': 'email',
			'first_name': 'first name',
			'last_name': 'last name',
			'ssn': 'last four number ssn id',
			'classification': 'classification for nurse',
			'address': 'adress',
			'city': 'city',
			'state': 'state',
			'zip_code': 'zip code',
			'phone': 'phone',
			'hire_date': 'hire date',
			'term_date': 'term date',
			'sex': 'sex',
			'race': 'race',
			'job_category': 'job category',
			'dob': 'date of birth',
			'photo_url': 'photo url',
			'pay_differential': 'pay differential',
			'evening_differential': 'evening differential',
			'weekend_differential': 'weekend differential',
			'license_1': 'license 1',
			'license_1_state': 'license 1 state',
			'contract_hospital': 'contract hospital',
			'contract_start': 'contract start',
			'contract_stop': 'contract stop',
			'paychex_id': 'paychex id'
		}
	}
