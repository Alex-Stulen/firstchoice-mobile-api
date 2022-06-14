# Nurse remove file for Core Credentials. Only for: ('PPD', 'BLS', 'Urine Drug Screen', 'Flu Vaccine')
'https://dev.firstchoicenurses.com/api/v1/mobile/api/v1/mobile/obj/nurse/core-credential/remove-file'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields = {
	'file_id': <type: integer. ID for file record in DB. Required>
}

returns = {'status': 'ok'} or {'status': 'fail', 'detail': '...some error detail...'}