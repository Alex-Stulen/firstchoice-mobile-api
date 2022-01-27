# Search Nurse by fname or lname fields
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/search?fname=...&lname=...'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = {
	'fname': <type: string. Optional>,
	'lname': <type: string. Optional>
}

returns = 'returns array with nurse objects'
