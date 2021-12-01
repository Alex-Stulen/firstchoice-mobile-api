# Update current Nurse Profile info

def UpdateNurseProfileInfo():

	api_url = 'https://firstchoicenurses.com/api/v1/mobile/obj/nurse/profile/update'
	method = 'PATCH'
	headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
	patch_fields = 'can contain this fields':('email', 'fname', 'lname', 'ssn', 'classification', 'address', 'city',
		          'st', 'zipcode', 'phone', 'phone2', 'hire_date', 'term_date', 'dob', 'photo')
		# Note: all fields is string type.
		# photo - path to avatar file.
		example:{
			"fname": "TestTest",
			"lname": "LastLast",
			"hire_date": "2021-04-12",
			"term_date": null
			"photo": "/uploads/avatar/vfnams/doctor-nurse.jpg"
		}

	returns = example: {
		    "email": "some@gmail.com",
		    "fname": "TestTest",
		    "lname": "LastLast",
		    "ssn": "111-22-3333",
		    "classification": "test",
		    "address": "test",
		    "city": "test",
		    "st": "va",
		    "zipcode": "",
		    "phone": "",
		    "phone2": "",
		    "hire_date": "2021-04-12",
		    "term_date": null,
		    "photo": "/uploads/avatar/vfnams/doctor-nurse.jpg"
		    "dob": "2021-10-06"
		}

