# Nurse get info about Core Credential record
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/core-credential/get-info/<int:core_cred_id>'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = '<int:core_cred_id> in request url'

for 'Urine Drug Screen' core cred:
    returns = {
        "title": "Urine Drug Screen",
        "date_completed_results": 1655067600,
        "result": "TESssssssT",
        "notes": "TEST NOTES",
        "files": [
            {
                "id": 31,
                "file_url": "/uploads/vaccine/test.jpg"
            },
            ...
        ]
    }

for 'Flu Vaccine':
    returns = {
        "title": "Flu Vaccine",
        "expiration_date": 1654981200,
        "notes": "TEST NOTEsssssS",
        "declination_bool": true,
        "files": [
            {
                "id": 31,
                "file_url": "/uploads/vaccine/test.jpg"
            },
            ...
        ]
    }

for 'PPD' core cred:
    returns = {
        "title": "PPD",
        "ppd_type": null,
        "expiration_date": 1655067600,
        "notes": "TEST NOTEsssssSdasdasd",
        "files": [
            {
                "id": 31,
                "file_url": "/uploads/vaccine/test.jpg"
            }
        ],
        "ppd_allowed_types": [
            null,
            "XRay",
            "PPD 1",
            "PPD 2",
            "TB Screening"
        ]
    }

for 'BLS' core cred:
    returns = {
        "title": "BLS",
        "expiration_date": 1655067600,
        "notes": "TEST NOTEsssssSdasdasd",
        "files": [
            {
                "id": 33,
                "file_url": "/uploads/vaccine/test.jpg"
            },
            ...
        ]
    }

for 'Professional License' core cred:
    returns = {
        "type": "CNA",
        "expiration_date": 1655067600,
        "state": "AK",
        "note": "",
        "chose_file": "/uploads/vaccine/test.jpg",
        "core_cred_id": 3,
        "title": "Professional License",
        "allowed_states": [
            null,
            "AK",
            "AL",
            "AR",
            "AZ",
            "CA",
            "CO",
            "CT",
            "DC",
            "DE",
            "FL",
            "GA",
            "HI",
            "IA",
            "ID",
            "IL",
            "IN",
            "KS",
            "KY",
            "LA",
            "MA",
            "MD",
            "ME",
            "MI",
            "MN",
            "MO",
            "MS",
            "MT",
            "NC",
            "ND",
            "NE",
            "NH",
            "NJ",
            "NM",
            "NV",
            "NY",
            "OH",
            "OK",
            "OR",
            "PA",
            "PR",
            "RI",
            "SC",
            "SD",
            "TN",
            "TX",
            "UT",
            "VA",
            "VT",
            "WA",
            "WI",
            "WV",
            "WY"
        ],
        "allowed_types": [
            null,
            "CNA",
            "LPN",
            "RN"
        ]
    }

for 'Identifying Documents' core cred:
    returns = {
    "allowed_document_dropdowns": [
        "Government Issued ID",
        "Social Security Card",
        "Passport",
        "Birth Certificate",
        "Other"
    ],
    "documents": [
        {
            "id": 10,
            "document_dropdown": "Government Issued ID",
            "name_of_the_id": "test",
            "name_of_the_document": null <type: string or null>,
            "expiration_date": 1655758800,
            "chose_file": null <type: string or null>,
            "core_credential": 1
        }
    ]
}

for 'License Loop Up' core cred:
    # if res_type == 'others' -> response contain 'others' field (type: array with other objects)
    # if res_type == 'object' -> response contain 'object' field (type: dict for Python, object for JS with object data)

    returns = {
    "res_type": "others",
    "allowed_types": [
        "CNA",
        "LPN",
        "RN",
        "other"
    ],
    "allowed_states": [
        null,
        "AK",
        "AL",
        "AR",
        "AZ",
        "CA",
        "CO",
        "CT",
        "DC",
        "DE",
        "FL",
        "GA",
        "HI",
        "IA",
        "ID",
        "IL",
        "IN",
        "KS",
        "KY",
        "LA",
        "MA",
        "MD",
        "ME",
        "MI",
        "MN",
        "MO",
        "MS",
        "MT",
        "NC",
        "ND",
        "NE",
        "NH",
        "NJ",
        "NM",
        "NV",
        "NY",
        "OH",
        "OK",
        "OR",
        "PA",
        "PR",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UT",
        "VA",
        "VT",
        "WA",
        "WI",
        "WV",
        "WY"
    ],
    "others": [
        {
            "id": 13,
            "type": "other",
            "note": null <type: string or null>,
            "state": null <type: string or null>,
            "expiration_date": null <type int or null. Timestamp>,
            "chose_file": null <type: string or null>
        }
    ],
    "core_credential_id": 2
}
