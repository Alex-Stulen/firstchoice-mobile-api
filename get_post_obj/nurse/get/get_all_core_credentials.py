# Nurse get all Core Credential records
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/get-all-core-credentials'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed'

returns = [
		{
			"id": <integer: some id>,
			"title": "Identifying Documents",
			"expiration_date": 1654722000,
			"notes": "None"
		},
		{
			"id": <integer: some id>,
			"title": "PPD",
			"expiration_date": 1655067600,
			"notes": "None"
		},
		{
			"id": <integer: some id>,
			"title": "Professional License",
			"expiration_date": "None",
			"notes": "None"
		},
		{
			"id": <integer: some id>,
			"title": "BLS",
			"expiration_date": 1655067600,
			"notes": "None"
		},
		{
			"id": <integer: some id>,
			"title": "License Look Up",
			"expiration_date": "None",
			"notes": "None"
		},
		{
			"id": <integer: some id>,
			"title": "Urine Drug Screen",
			"expiration_date": "None",
			"notes": "TESssssssT"
		},
		{
			"id": <integer: some id>,
			"title": "Flu Vaccine",
			"expiration_date": 1654981200,
			"notes": "Declined"
		}
	]
