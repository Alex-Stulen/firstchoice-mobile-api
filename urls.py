# API urls examples
# Note: all requests in the examples are directed to the development site

"""===================================================================="""

# Login
'https://dev.firstchoicenurses.com/api/v1/mobile/auth/login'
method = 'POST'
headers = 'special headers are not needed'
post_fields = {
    "email": "testnurse@gmail.com",
    "password": "qwertY11"
}

returns = {
    "password_is_valid": true,
    "Token": "9e4dd75530d78369330296e00905a84eed69af6f",
    "user": {
        "pk": 4065,
        "role": "nurse"
    },
    "authorized": true,
    "email_is_valid": true
}

""" For facility """
post_fields = {
    "email": "testfacility",
    "password": "testqwerty"
}

returns = {
    "password_is_valid": true,
    "Token": "294e355fe08b3713a4a2591aef682453204d3cb4",
    "user": {
        "pk": 29,
        "role": "facility"
    },
    "authorized": true,
    "email_is_valid": true
}


"""===================================================================="""

# Logout
'https://firstchoicenurses.com/api/v1/mobile/auth/logout'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed'

returns = {}


"""===================================================================="""

# Verification
'https://dev.firstchoicenurses.com/api/v1/mobile/auth/verification'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields = {
    "pk": "4065",
    "employee_id": "4321",
    "last_four_ssn": "1234"
}

returns = {
    "employee_id_is_valid": true,
    "last_four_ssn_is_valid": true,
    "Token": "9e4dd75530d78369330296e00905a84eed69af6f",
    "verified": true,
    "user": {
        "pk": 4065,
        "role": "nurse",
        "is_active_nurse": true
    }
}

"""===================================================================="""

# Verification by user Date of Birth

'https://dev.firstchoicenurses.com/api/v1/mobile/auth/verification-by-dob'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields = {
                'dob': <type: str>, template: '2021-01-01',
                'last_four_ssn': <type: str>, template: '1234'
            }

returns = 'Read Verification read the section above'

"""===================================================================="""

"""===================================================================="""

# Uploading files to the system

'https://dev.firstchoicenurses.com/api/v1/mobile/upload-files'
 OR
'https://dev.firstchoicenurses.com/api/v1/mobile/upload-files/<path:folder_paths>'
The first link will save the files to the global downloads folder
The second link will save the files to a specific folder at the specified path.
	Example:
		if you want to save files to a folder in a special path ('/<global folder for uploads:indicated automatically>/test/folder')
		in folder 'test/folder'.
		you must send a request to '/api/v1/mobile/upload-files/test/folder'
		
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH

returns = 'Read `get_shift.py`'

"""===================================================================="""


# Get current Nurse Detail info
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed'

returns = {
		'user': {
            '...'
        }
	}

"""===================================================================="""

# Create current Nurse Credential.
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/add-credential'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields = {
		'name': <type: string. Required>,
		'issue_date': <type: string. format: YYYY-MM-DD. Optional>, 
		'expire_date': <type: string. format: YYYY-MM-DD. Optional>, 
		'description': <type: string. Required>,
		'file': <type: string, path to file. Required> # should start with `/uploads/`
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

# Create current Nurse Education.
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/add-education'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields = {
		'name': <type: string. Required>,
		'date': <type: string. format: YYYY-MM-DD. Optional>, 
		'score': <type: string. string.Optional>, 
		'description': <type: string. Oprional>,
		'file': <type: string, path to file. Required> # should start with `/uploads/`
	}

returns = {
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
    }

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

# Update Nurse Credential.
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/update-credential/<int:credential_id>'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields = {
		'name': <type: string. Optional>,
		'issue_date': <type: string. format: YYYY-MM-DD. Optional>, 
		'expire_date': <type: string. format: YYYY-MM-DD. Optional>, 
		'description': <type: string. Optional>,
		'file': <type: string, path to file. Optional>
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

# Update Nurse Education.
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/update-education/<int:education_id>'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields = {
		'name': <type: string. Optional>,
		'date': <type: string. format: YYYY-MM-DD. Optional>, 
		'score': <type: string. string.Optional>, 
		'description': <type: string. Oprional> # should start with `/uploads/`
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

# Update Nurse Password
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/profile/change-password'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields = {
		"old_password": <type: string. Required>,
		"new_password1": <type: string. Required>,
		"new_password2": <type: string. Required>
	}

returns = {
    		"status": true
	}
	# Returns Note:
	#	The response body may vary depending on the result of the server.
	# 	Possible status answers (check response body):
	#		400 - Bad request or The query body does not contain an old password or a new password 1 or a new password 2.
	# 			check response body.
	#		404 - Nurse with this token does not exist.
	# 		403 - old_password != current nurse password or new_password1 != new_password2 (check response body).
	#		200 - OK. Password changed successfully
	# 		401 - Bad Auth Token. Check response body.
	

"""===================================================================="""


# Update current Nurse Profile info
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/profile/update'
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
		"photo": "/uploads/avatar/vfnams/doctor-nurse.jpg"
		"term_date": null
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

"""===================================================================="""


# Nurse assigned shifts
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/assigned-shifts'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed' 

returns = {
		'assigned_shifts': [
			{'the object is returned as if you made a request to receive detailed information about the shift. Read `get_shift.py`'},
			...,
			...,
			{'the object is returned as if you made a request to receive detailed information about the shift. Read `get_shift.py`'}
		]
	}

"""===================================================================="""

# Nurse assign to shift
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/assign-to-shift'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields = {
		"shift_id" <type: integer or string>
	} 

returns = {
		'assign_shift': {...}
	}

"""===================================================================="""

# Nurse cancel assign to shift
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/cancel-assign-to-shift'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields = {
		"shift_id" <type: integer or string>
	} 

returns = 'no content'

"""===================================================================="""

# Nurse submit shift
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/shift/<int:pk>/submit-by-nurse' # <int:pk> - primary key for shift
method = 'PUT'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields = {
                'submitted_nurse_shift_files': <type: list. Optional>,
                'fields for update shift'...
            }
            # Note:
            	'submitted_nurse_shift_files' - cannot be empty. Can contain one file path.
            	'submitted_nurse_shift_files' - is an array with file paths.
            	example:
            		{
            			'submitted_nurse_shift_files': ['/uploads/test/folder/test_icon.png']
            			 OR
            			'submitted_nurse_shift_files': ['/uploads/test/folder/file1.pdf', '/uploads/test/folder/file2.pdf', ...]
            		}

returns = {
	'shift data. Read `get_shift.py`'
}

"""===================================================================="""

# Nurse all past shifts
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/past-shifts'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed'

returns = {
		[...]
	}

"""===================================================================="""

# Nurse certified shifts
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/certified-shifts'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed' 

returns = {
		'certified_shifts': [
			{'the object is returned as if you made a request to receive detailed information about the shift. Read `get_shift.py`'},
			...,
			...,
			{'the object is returned as if you made a request to receive detailed information about the shift. Read `get_shift.py`'}
		]
	}

"""===================================================================="""

# Clock-in/CLock-out shift ability
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/shift/<int:pk>/(clock-in/clock-out)'
method = 'PATCH'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
patch_fields = {
        "latitude": <type: float>,
        "longitude": <type:float>,
    }

returns = {'shift object. Read `get_shift.py`'}

"""===================================================================="""

# Hospital list
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/hospital/list'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed'
returns = {'hospital list. Read `hospital_list.py`'}

"""==================================================================="""

# All shifts for special hospital
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/hospital/<int:pk>/all-shifts'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = {
            "pk": "<type: int> - primary key for special hospital"
        }
returns = {'list with shifts objects. Read `get_shift.py`'}

"""==================================================================="""

# Filter shifts by hospitals && internaFrom && internalTo
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/shift/filter?hospitals=1,2,3&internalFrom=1233412&internalTo=123123'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH

returns = {'short shift objects. Read `get_shift.py`'}

"""==================================================================="""

# Shift Update
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/shift/<int:pk>/update'
method = 'PUT'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
put_fields {'any fields for shift update; For example:',
            
            'classification': 'lololo',
            'comments': 'some comment',
            'cancelled': true
        }

returns = {'shift object. Read `get_shift.py`'}

"""=================================================================="""

# Generate Shift
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/generate-shift/'
method = 'GET'
headers = 'special headers are not needed'
get_fields = 'special get fields are not needed'

returns = {'shift object. Read `get_shift.py`'}

"""===================================================================="""
