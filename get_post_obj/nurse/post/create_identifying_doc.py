# Create Identifying Document instance
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/core-credential/identifying-documents/create/<int:core_cred_id>'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields_url = '<int:core_cred_id> - id for core credential. In request url. Required'
post_fields = {
            "document_dropdown": <type: string. Required>,
            "name_of_the_id": <type: string. Optional>,
            "name_of_the_document": <type: string. Optional>,
            "expiration_date": <type: int. Timestamp. Optional>,
            "files": <type: file. Optional>,
        }

returns = {'status': 'ok'} or {'status': 'fail', 'detail': '...some error detail...'}

"""===================================================================="""