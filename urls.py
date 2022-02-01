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

# Get current Facility Admin Detail info
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/admin-detail-info'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed'

returns = {
	    "id": 83,
	    "username": "testfacility",
	    "first_name": "",
	    "last_name": "",
	    "email": "testfacility@gmail.com",
	    "date_joined": "2022-01-18T15:07:32.779427-05:00"
	}

"""===================================================================="""

# Get all hospitals ids for current facility admin
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/all-admin-hospitals'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed'

returns = [
	    {
		"id": 999,
		"name": "Test Test"
	    }
	]


"""===================================================================="""

# Get all future shifts for special facility
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/<int:facility_id>/get-future-shifts'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed'

returns = [  # array with objects
	    {
		"id": 199898,
		"comments": "TEST",
		"timestamp": "2022-01-18T15:56:20.247043-05:00",
		"submitted_by_nurse": false,
		"submitted_by_nurse_timestamp": "2022-01-18T15:56:20.247065-05:00",
		"is_draft": false,
		"cancelled": false,
		"certified": false,
		"certified_on": null,
		"start_datetime": "2022-01-19T15:00:00-05:00",
		"stop_datetime": "2022-01-19T23:00:00-05:00",
		"clock_in_at": null,
		"clock_in_location": "",
		"clock_in_latitude": null,
		"clock_in_longitude": null,
		"clock_out_at": null,
		"clock_out_location": "",
		"clock_out_latitude": null,
		"clock_out_longitude": null,
		"daylight_saving_time": "undefined",
		"duration": "08:00:00",
		"regular_duration": null,
		"break_duration": null,
		"overtime_duration": null,
		"holiday_duration": null,
		"import_lock": false,
		"client": "NANSPT",
		"department": "ORIENT",
		"date": "2022-01-19",
		"classification": "LPN",
		"ordered_by": "Gennette - Staff Developm",
		"received": "2022-01-18T15:56:20.216494-05:00",
		"received_by": "admin",
		"assigned": null,
		"assigned_by": "",
		"first_assigned": null,
		"confirmed": null,
		"confirmed_by": "",
		"confirmed_to": "",
		"shift": "03PM-11PM",
		"start_time": 1500,
		"stop_time": 2300,
		"regular_hours": null,
		"break_hours": null,
		"overtime_hours": null,
		"holiday_hours": null,
		"travel": null,
		"check_date": null,
		"check_number": null,
		"check_amount": null,
		"invoice_number": null,
		"invoice_date": null,
		"invoice_amount": null,
		"ok_to_bill": false,
		"ok_overtime": true,
		"exported": false,
		"site": "NEWPO",
		"paychex_id": null,
		"worker": "",
		"keyfield": "0c04fd01-52fa-4ff5-b9cf-a1a37b1f6c21",
		"hospital": 14,
		"profile": null,
		"nurse": 3971,
		"accepted_nurse": null,
		"certified_by": null,
		"received_by_user": 23,
		"assigned_by_user": null,
		"first_assigned_by_user": null,
		"booked": []
	    },
	    ...
    ]


"""===================================================================="""

# Set special shift as certified
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/shift/<int:shift_id>/set-as-certified'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields = {
	'is_certified': <type: bool. Required. Can only be equal as true>
	}
	
returns = {
		'status': 'ok'
	}
	
or returns if request is BAD = {
				'detail': <detail info about error>,
				'status': 'fail'
				}
				

"""===================================================================="""

# Set special shift as rejected
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/shift/<int:shift_id>/set-as-rejected'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields = {
	'is_rejected': <type: bool. Required. Can only be equal as true>
	}
	
returns = {
		'status': 'ok'
	}
	
or returns if request is BAD = {
				'detail': <detail info about error>,
				'status': 'fail'
				}
				

"""===================================================================="""

# Get all shifts by special status
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/shift/get-all-by-status?status=...'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
allowed statuses = ['pending', 'certified', 'rejected']
get_fields = {
	'status': <type: str. Required>
	}
	
returns = 'returns array with shift objects. Can be empty'


"""===================================================================="""

# Get all shifts by special status for special hospital
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/shift/<int:facility_id>/get-all-by-status?status=...'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
allowed statuses = ['pending', 'certified', 'rejected']
get_fields = {
	'status': <type: str. Required>
	}
	
returns = 'returns array with shift objects. Can be empty'
    
    
"""===================================================================="""

# Get detail info about special hospital
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/hospital/<int:hospital_id>/detail-info'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed'

returns = { # returns error 404 if hospital does not exist
	    "id": 14,
	    "username": null,
	    "email": null,
	    "password": null,
	    "comments": null,
	    "timestamp": 1575578382,
	    "shortcode": "NANSPT",
	    "name": "Nansemond Pointe Rehab & Healthcare",
	    "attention": null,
	    "address": "200 W. Constance Rd.",
	    "address2": null,
	    "city": "Suffolk",
	    "st": "VA",
	    "zipcode": "23434",
	    "contact": "Gennette - Staff Developme",
	    "phone": "+17575398744",
	    "phone1": "+17575396128",
	    "phone2": "",
	    "phone3": "",
	    "vfemail": "Admin- Mel Appelle\r\nDON-\r\n",
	    "vfcomments": " go I -64 towards suffolk -   downtown suffolk exit, follow a little bit down to you see McDonalds pass McDonalds  2nd driveway on your right W. Constance ( sign back a little )",
	    "show_aging": true,
	    "facility_type": "Facility",
	    "account_representative": "",
	    "invoice_method": "C",
	    "early_pay_discount_rate": "0.0000",
	    "early_pay_due": 0,
	    "invoice_due": 35,
	    "invoice_late_rate": "1.5000",
	    "invoice_late_fee": "0.00",
	    "factoring_agent": "ADVANCE",
	    "auto_add_travel": false,
	    "round_invoice_hours": false,
	    "site": "NEWPO",
	    "covid_vaccine": false,
	    "notes": null,
	    "covid_exemption": false,
	    "notes_for_covid_exemption": null
	}

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

# Search Nurse by fname or lname fields
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/search?fname=...&lname=...'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = {
	'text': <type: string. Required>,
	'page': <type: int. Optional. Default equal 1>
}


returns = {
    "total_pages": <type: int>,
    "current_page": <type: int>,
    "data": <type: array. Array with nurses objects>
}

"""===================================================================="""

# Get special Nurse detail info
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/<int:nurse_id>/detail-info'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed'

returns = 'returns detail info about nurse. Read `get_nurse_detail_info.py`'

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

# Book nurse to shift
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/shift/<int:shift_pk>/booked'
method = 'PUT'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
put_fields = 'special put fields are not needed'

returns = 'returns shift short info'

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

# (for facility admin) Nurse assign to shift
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/nurse/<int:nurse_id>/assign-to-shift'
method = 'PUT'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
put_fields = {
	"shift_id": <type: integer. Required>
	}

returns = 'assigned shift object'

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

# Filter shifts by hospitals && internaFrom && internalTo without nurse by token
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/shift/filter?hospitals=1,2,3&internalFrom=1233412&internalTo=123123'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH

returns = {'short shift objects. Read `get_shift.py`'}

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
