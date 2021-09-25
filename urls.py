# API urls examples
# Note: all requests in the examples are directed to the development site

"""===================================================================="""

# Login
'https://dev.firstchoicenurses.com/api/v1/mobile/login/'
method = 'POST'
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

"""===================================================================="""

# Verification
'https://dev.firstchoicenurses.com/api/v1/mobile/verification/'
method = 'POST'
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

