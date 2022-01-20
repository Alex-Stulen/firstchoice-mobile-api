# Get all hospitals ids for current facility admin
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/all-admin-hospitals'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed'

returns = 'array with hospitals ids'
