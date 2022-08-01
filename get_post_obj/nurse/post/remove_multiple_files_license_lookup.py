# Remove multiple files for License Look Up by ids. Only for CNA, LPN and RN types
'/api/v1/mobile/obj/nurse/core-credential/update/license-look-up/<int:core_cred_id>/remove-multiple-files'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields_url = '<int:core_cred_id> - id for core credential. In request url. Required'
post_fields = {
	"file-ids": [<type: int>, <type: int>, ...] # Insert sub_core object id
}

returns = {'status': 'ok'} or {'status': 'fail'}

"""===================================================================="""