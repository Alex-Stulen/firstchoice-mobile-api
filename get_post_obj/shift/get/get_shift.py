# Get detail shift info


def Get_Shift():

	"""
		Note:
			to get information about a shift, you do not need to specify the fields for a get request. 
			It is enough to specify the primary key of the shift in the address bar instead of <pk>.
	"""
	api_utl = 'https://firstchoicenurses.com/api/v1/mobile/obj/shift/<pk>/'

	method = 'GET'
	headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH

	get_fields = 'special get fields are not needed'

	# WARNING: 
	#	At the moment, the response data given in the documentation does not match what is being returned. 
	#	In a short time the documentation will be updated.
	returns = {
		'shift': {
			'hospital':{
				'name': '<type: str>',
				'pk': 'primary key'
			},
			'comments': '<type: str>',
			'nurse': {
				'pk': 'primary key',
			},
			'cancelled': '<type: bool>',
			'certified': '<type: bool>',
			'certified_by': {
				'user':{
					'pk': 'primary key',
					'username': '<type: str>'
				}
			},
			'certified_on': {
				'year': '<type: int>',
				'month': '<type: int>',
				'day': '<type: int>',
				'time': '<type: str>'
			},
			'start_datetime': {
				'year': '<type: int>',
				'month': '<type: int>',
				'day': '<type: int>',
				'time': '<type: str>'
			},
			'stop_datetime': {
				'year': '<type: int>',
				'month': '<type: int>',
				'day': '<type: int>',
				'time': '<type: str>'
			},
			'daylight_saving_time': '<type: str>',
			'duration': {
				'hours': '<type: int>',
				'minutes': '<type: int>',
				'seconds': '<type: int>'
			}
			'regular_duration': {
				'hours': '<type: int>',
				'minutes': '<type: int>',
				'seconds': '<type: int>'
			},
			'break_duration': {
				'hours': '<type: int>',
				'minutes': '<type: int>',
				'seconds': '<type: int>'
			},
			'overtime_duration': {
				'hours': '<type: int>',
				'minutes': '<type: int>',
				'seconds': '<type: int>'
			},
			'holiday_duration': {
				'hours': '<type: int>',
				'minutes': '<type: int>',
				'seconds': '<type: int>'
			},
			'client': '<type: str>',
			'department': '<type: str>',
			'date': '<type: str>',
			'classification': '<type: str>',
			'ordered_by': '<type: str>',
			'received': {'<type: int>',
			'received_by': 'received by <type: str>',
			'shift': '<type: str>',
			'start_time': '<type: int>',
			'stop_time': '<type: int>',
			'regular_hours': '<type: float>',
			'break_hours': '<type: float>',
			'overtime_hours': '<type: float>',
			'holiday_hours': '<type: float>',
			'travel': '<type: float>',
			'check_date': '<type: str>',
			'check_number': '<type: int>',
			'check_amount': '<type: float>',
			'invoice_number': '<type: str>',
			'invoice_date': '<type: str>'
			'invoice_amount': '<type: float>',
			'ok_to_bill': '<type: bool>',
			'ok_overtime': '<type: bool>',
			'exported': '<type: bool>',
			'site': '<type: str>',
			'paychex_id': '<type: int>',
			'worker': '<type: str>',
			'keyfield': '<type: str>',
			'timestamp': '<type: int>'
		}
	}

