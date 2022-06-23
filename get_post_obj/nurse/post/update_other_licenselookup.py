# Update other for License Look Up
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/core-credential/update/license-look-up/other/update/<int:other_id>'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields_url = '<int:other_id> - id for other object. In request url. Required'
post_fields = {
    "note": <type: string. MaxLength: 2048. Optional>,
    "state": <type: string. MaxLength: 2, Optional>,
    "expiration_date": <type: int. Timestamp. Optional>,
    'files': <type: array. Array with paths to uploaded file. Optional>
}

returns = {
    "status": "ok",
    "object": {
        "id": 13,
        "type": "other",
        "note": null,
        "state": null,
        "expiration_date": null,
        "chose_file": null,
        "sub_core_credential": 12
    }
}

"""===================================================================="""
