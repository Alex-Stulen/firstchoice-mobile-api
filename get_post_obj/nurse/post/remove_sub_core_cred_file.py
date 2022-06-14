# Nurse remove file for Core Credentials. Only for: ('Professional License')
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/core-credential/sub-core/remove-file'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields = {
	'sub_core_id': <type: integer. ID for sub core record in DB>
}
returns = {'status': 'ok'} or {'status': 'fail', 'detail': '...some error detail...'}
