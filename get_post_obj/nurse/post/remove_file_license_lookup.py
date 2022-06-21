# Remove file for Look Up instance. Only for CNA, LPN and RN types
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/core-credential/update/license-look-up/<int:core_cred_id>/remove-file'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields_url = '<int:core_cred_id> - id for core credential. In request url. Required'
post_fields = 'no need'

returns = {'status': 'ok'} or {'status': 'fail'}

"""===================================================================="""
