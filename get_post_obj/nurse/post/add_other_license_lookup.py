# Add other for License Look Up instance
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/core-credential/update/license-look-up/<int:core_cred_id>/add-other'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields_url = '<int:core_cred_id> - id for core credential. In request url. Required'
post_fields = {
    "note": <type: string. MaxLength: 2048. Optional>,
    "state": <type: string. MaxLength: 2, Optional>,
    "expiration_date": <type: int. Timestamp. Optional>,
    "chose_file": <type: file. Optional>
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
    },
    "core_credential_pk": 2
}

"""===================================================================="""
