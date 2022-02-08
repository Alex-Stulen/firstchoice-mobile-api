# Get all classifications for special hospital
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/hospital/<int:hospital_id>/get-all-classifications'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed'

returns = [
    {
        "classification": "TEST",
        "classification_count": 37
    },
    {
        "classification": "TEST",
        "classification_count": 0
    }
]
