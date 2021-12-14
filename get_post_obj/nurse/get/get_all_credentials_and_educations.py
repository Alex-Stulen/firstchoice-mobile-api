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
		"score": "11",
		"name": "Test education",
		"file": "/uploads/education/Screenshot_from_2021-09-30_14-13-29.png",
		"worker": {
		    "id": 4065,
		    "fname": "Test nursest",
		    "lname": "Nurse",
		    "email": "testnurse@gmail.com",
		    "phone": "1111111111111111",
		    "dob": "2021-05-05",
		    "photo": "/uploads/avatar/vfnams/doctor-nurse.jpg"
		},
		"description": "sdf",
		"date": "2021-08-11",
		"id": 5,
		"education": 5,
		"user": null
	    },
		
		...
	]

"""===================================================================="""
