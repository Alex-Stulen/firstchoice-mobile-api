'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/core-credential/update/<int:core_cred_id>'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_url_fields = '<int:core_cred_id> in request url'
for 'Urine Drug Screen' core cred:
	post_fields = {
		'date_completed_results': <type: integer. Timestamp. Optional>,
		'result': <type: string, Optional>,
		'notes': <type: string, Optional>,
	  	'files': <type: array. Array with paths to uploaded file. Optional>
	}

for 'Flu Vaccine' core cred:
	post_fields = {
		'expiration_date': <type: integer, Timestamp, Optional>,
		'notes': <type: string. Optional>,
		'declination_bool': <type: bool, Optional>,
	  	'files': <type: array. Array with paths to uploaded file. Optional>
	}

for 'PPD' core cred:
	post_fields = {
		'ppd_type': <type: string or null. Optional>,
		'expiration_date': <type: integer, Timestamp, Optional>,
		'notes': <type: string. Optional>,
	  	'files': <type: array. Array with paths to uploaded file. Optional>
	}

for 'BLS' core cred:
	post_fields = {
	  'expiration_date': < type: integer, Timestamp, Optional >,
	  'notes': < type: string.Optional>,
	  	'files': <type: array. Array with paths to uploaded file. Optional>
	}

for 'Professional License' core cred:
	post_fields = {
		'type': < type: string or null.Optional>,
	  	'expiration_date': < type: integer, Timestamp, Optional >,
		'state': <type: string or null. Optional>,
		'note': <type: string, Optional>,
	  	'files': <type: array. Array with paths to uploaded file. Optional>
	}

	returns = {'status': 'ok'} or {'status': 'fail', 'detail': '...some error detail msg...'}

for 'License Look Up (exclude 'other' type)' core cred:
	# you cannot update this core credential if it is a list of other

	post_fields = {
		"type": < type: string.Only CNA, LPN or RN.Required >,
		"note": < type: string.MaxLength: 2048. Optional >,
		"state": < type: string.MaxLength: 2, Optional >,
		"expiration_date": < type: int.Timestamp.Optional >,
		'files': <type: array. Array with paths to uploaded file. Optional>
	}

	returns = {
		"status": "ok",
		"object": {
			"id": 12,
			"type": "CNA",
			"note": null,
			"state": "VA",
			"expiration_date": 1655672400,
			"chose_file": "/uploads/core_credentials/Image_upload_test_lkwl9wn.jpg"
		},
		"core_credential_pk": 2
	}
