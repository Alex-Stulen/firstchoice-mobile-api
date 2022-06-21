# Remove file only for other for License Look Up
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/core-credential/update/license-look-up/other/<int:other_id>/remove-file'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields_url = '<int:other_id> - id for other object. In request url. Required'
post_fields = 'no need'

returns = {'status': 'ok'} or {'status': 'fail'}

"""===================================================================="""
