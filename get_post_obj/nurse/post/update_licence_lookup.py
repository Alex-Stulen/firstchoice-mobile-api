# Update License Look Up instance. Only for CNA, LPN and RN types
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/core-credential/update/license-look-up/<int:core_cred_id>'
method = 'POST'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
post_fields_url = '<int:core_cred_id> - id for core credential. In request url. Required'
post_fields = {
    "type": <type: string. Only CNA, LPN or RN. Required>,
    "note": <type: string. MaxLength: 2048. Optional>,
    "state": <type: string. MaxLength: 2, Optional>,
    "expiration_date": <type: int. Timestamp. Optional>,
    "chose_file": <type: file. Optional>
}

returns = {
        "status": "ok",
        "object": {
            "id": 12,
            "type": "CNA",
            "note": null,
            "state": "VA",
            "expiration_date": 1655672400,
            "chose_file": "/uploads/core_credentials/Image_upload_test_lkwl9wn.jpg"
        },
        "core_credential_pk": 2
    }

"""===================================================================="""
