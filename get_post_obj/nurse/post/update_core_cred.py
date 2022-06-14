'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/core-credential/update/<int:core_cred_id>'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_url_fields = '<int:core_cred_id> in request url'
for 'Urine Drug Screen' core cred:
	post_fields = {
		'date_completed_results': <type: integer. Timestamp. Optional>,
		'result': <type: string, Optional>,
		'notes': <type: string, Optional>,
		'file': <type: string. Path to uploaded file. Optional>
	}

for 'Flu Vaccine' core cred:
	post_fields = {
		'expiration_date': <type: integer, Timestamp, Optional>,
		'notes': <type: string. Optional>,
		'declination_bool': <type: bool, Optional>,
		'file': <type: string. Path to uploaded file. Optional>
	}

for 'PPD' core cred:
	post_fields = {
		'ppd_type': <type: string or null. Optional>,
		'expiration_date': <type: integer, Timestamp, Optional>,
		'notes': <type: string. Optional>,
		'file': <type: string. Path to uploaded file. Optional>
	}

for 'BLS' core cred:
	post_fields = {
	  'expiration_date': < type: integer, Timestamp, Optional >,
	  'notes': < type: string.Optional>,
	  'file': <type: string. Path to uploaded file. Optional>
	}

for 'Professional License' core cred:
	post_fields = {
		'type': < type: string or null.Optional>,
	  	'expiration_date': < type: integer, Timestamp, Optional >,
		'state': <type: string or null. Optional>,
		'note': <type: string, Optional>,
		'chose_file': <type: file. Optional>
	}

returns = {'status': 'ok'} or {'status': 'fail', 'detail': '...some error detail msg...'}