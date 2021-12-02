# Get All Nurse Credential.
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/get-all-credentials'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed'

returns = [
		{
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
		},
		
		...
	]

"""===================================================================="""


# Get All Nurse Education.
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/get-all-educations'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed'

returns = [
		{
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
		},
		
		...
	]

"""===================================================================="""
