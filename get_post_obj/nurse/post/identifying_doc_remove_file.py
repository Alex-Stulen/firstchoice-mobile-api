# Remove file for Identifying Document instance
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/core-credential/identifying-documents/<int:document_id>/remove-file'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields_url = '<int:document_id> - id for document. In request url. Required'
post_fields = 'no need'

returns = {'status': 'ok'} or {'status': 'fail', 'detail': '...some error detail...'}

"""===================================================================="""
