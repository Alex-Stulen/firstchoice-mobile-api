# Create current Nurse Credential.
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/add-credential'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields = {
		'name': <type: string. Required>,
		'issue_date': <type: string. format: YYYY-MM-DD. Optional>, 
		'expire_date': <type: string. format: YYYY-MM-DD. Optional>, 
		'description': <type: string. Required>,
		'file': <type: file. Required>
	}

returns = {
	    "user": 74,
	    "worker": {
		"id": 5541,
		"fname": "Test",
		"lname": "Test",
		"email": "test@gmail.com",
		"phone": "",
		"dob": "2021-10-06",
		"photo": "/uploads/avatar/vfnams/doctor-nurse.jpg"
	    },
	    "name": "Test",
	    "issue_date": null,
	    "expire_date": null,
	    "description": "Test Test",
	    "credential": 114,
	    "file": "/uploads/credentials/ddd_oXNorw9.png"
	}

"""===================================================================="""

# Create current Nurse Education.
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/add-education'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields = {
		'name': <type: string. Required>,
		'date': <type: string. format: YYYY-MM-DD. Optional>, 
		'score': <type: string. string.Optional>, 
		'description': <type: string. Oprional>
	}

returns = {
	    "user": 74,
	    "worker": {
		"id": 5541,
		"fname": "Test",
		"lname": "Test",
		"email": "test@gmail.com",
		"phone": "",
		"dob": "2021-10-06",
		"photo": "/uploads/avatar/vfnams/doctor-nurse.jpg"
	    },
	    "name": "Test",
	    "date": "2020-10-23",
	    "score": "",
	    "description": ""
	}

"""===================================================================="""
