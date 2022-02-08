# Get departments for special hospital
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/dept/dept/<int:hospital_id>/get-all-departments'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed'

returns = 'returns detail info about departments. Read `get_all_depts.py`'
