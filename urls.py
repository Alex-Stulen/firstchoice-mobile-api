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
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/shift/filter'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields {
            'hospitals_id': <type: list>,
            'internalFrom': <type: int>,
            'internalTo': <type: int>
        }

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
