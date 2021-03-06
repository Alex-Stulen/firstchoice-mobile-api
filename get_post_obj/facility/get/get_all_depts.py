# Get all departments records
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/dept/get-all-departments?page=...'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = {
		'page': <type: integer. Optional. Default = 1>
	}

returns = {
    "total_pages": 28,
    "current_page": 1,
    "page_size": 20,
    "data": [
        {
            "id": 289,
            "client": "BARRYR",
            "deptid": "STANDBY",
            "dept": "",
            "billctr": "",
            "manager": "",
            "phone": "",
            "billytd": "0.00",
            "skillcode": "",
            "site": "NEWPO",
            "default": false,
            "timestamp": 1575578382,
            "facility": 24
        },
        {
            "id": 532,
            "client": "LUCY C",
            "deptid": "STANDBY",
            "dept": "",
            "billctr": "",
            "manager": "",
            "phone": "",
            "billytd": "0.00",
            "skillcode": "",
            "site": "RICH",
            "default": false,
            "timestamp": 1575578382,
            "facility": 66
        },
        {
            "id": 475,
            "client": "BETA",
            "deptid": "SKILLS",
            "dept": "",
            "billctr": "",
            "manager": "Hope Justice",
            "phone": "+18046722300",
            "billytd": "0.00",
            "skillcode": "MS",
            "site": "RICH",
            "default": false,
            "timestamp": 1575578382,
            "facility": null
        },
        {
            "id": 382,
            "client": "RREHAB",
            "deptid": "STANDBY",
            "dept": "",
            "billctr": "",
            "manager": "",
            "phone": "",
            "billytd": "197.63",
            "skillcode": "",
            "site": "NEWPO",
            "default": false,
            "timestamp": 1575578382,
            "facility": 41
        },
        {
            "id": 134,
            "client": "LADY",
            "deptid": "CHRISTO",
            "dept": "",
            "billctr": "",
            "manager": "",
            "phone": "",
            "billytd": "0.00",
            "skillcode": "",
            "site": "NEWPO",
            "default": false,
            "timestamp": 1575578382,
            "facility": null
        },
        {
            "id": 217,
            "client": "CRENSH",
            "deptid": "FRANK",
            "dept": "",
            "billctr": "",
            "manager": "",
            "phone": "",
            "billytd": "0.00",
            "skillcode": "",
            "site": "NEWPO",
            "default": false,
            "timestamp": 1575578382,
            "facility": null
        },
        {
            "id": 313,
            "client": "BRAND",
            "deptid": "STANDBY",
            "dept": "",
            "billctr": "",
            "manager": "",
            "phone": "",
            "billytd": "0.00",
            "skillcode": "",
            "site": "NEWPO",
            "default": false,
            "timestamp": 1575578382,
            "facility": null
        },
        {
            "id": 524,
            "client": "",
            "deptid": "",
            "dept": "",
            "billctr": "",
            "manager": "",
            "phone": "",
            "billytd": "0.00",
            "skillcode": "",
            "site": "",
            "default": false,
            "timestamp": 1575578382,
            "facility": null
        },
        {
            "id": 316,
            "client": "EJONES",
            "deptid": "STANDBY",
            "dept": "",
            "billctr": "",
            "manager": "",
            "phone": "",
            "billytd": "0.00",
            "skillcode": "",
            "site": "NEWPO",
            "default": false,
            "timestamp": 1575578382,
            "facility": null
        },
        {
            "id": 301,
            "client": "HARBOR",
            "deptid": "STANDBY",
            "dept": "",
            "billctr": "",
            "manager": "",
            "phone": "",
            "billytd": "0.00",
            "skillcode": "",
            "site": "NEWPO",
            "default": false,
            "timestamp": 1575578382,
            "facility": 5
        },
        {
            "id": 263,
            "client": "CGHOSP",
            "deptid": "PCU",
            "dept": "",
            "billctr": "",
            "manager": "Lisa Carroll",
            "phone": "",
            "billytd": "0.00",
            "skillcode": "",
            "site": "NEWPO",
            "default": false,
            "timestamp": 1575578382,
            "facility": null
        },
        {
            "id": 425,
            "client": "FIELDS",
            "deptid": "FIELDS",
            "dept": "",
            "billctr": "",
            "manager": "",
            "phone": "",
            "billytd": "0.00",
            "skillcode": "",
            "site": "NEWPO",
            "default": false,
            "timestamp": 1575578382,
            "facility": null
        },
        {
            "id": 426,
            "client": "RIVER",
            "deptid": "STANDBY",
            "dept": "",
            "billctr": "",
            "manager": "",
            "phone": "",
            "billytd": "0.00",
            "skillcode": "",
            "site": "NEWPO",
            "default": false,
            "timestamp": 1575578382,
            "facility": 6
        },
        {
            "id": 423,
            "client": "ROSEHI",
            "deptid": "STANDBY",
            "dept": "",
            "billctr": "",
            "manager": "",
            "phone": "",
            "billytd": "0.00",
            "skillcode": "",
            "site": "NEWPO",
            "default": false,
            "timestamp": 1575578382,
            "facility": 52
        },
        {
            "id": 422,
            "client": "MARYVI",
            "deptid": "ORIENT",
            "dept": "",
            "billctr": "",
            "manager": "",
            "phone": "",
            "billytd": "0.00",
            "skillcode": "",
            "site": "NEWPO",
            "default": false,
            "timestamp": 1575578382,
            "facility": 34
        },
        {
            "id": 340,
            "client": "MEADE",
            "deptid": "ORIENT",
            "dept": "",
            "billctr": "",
            "manager": "",
            "phone": "",
            "billytd": "24.50",
            "skillcode": "",
            "site": "NEWPO",
            "default": false,
            "timestamp": 1575578382,
            "facility": 33
        },
        {
            "id": 252,
            "client": "CHKD",
            "deptid": "7C",
            "dept": "",
            "billctr": "",
            "manager": "",
            "phone": "",
            "billytd": "0.00",
            "skillcode": "",
            "site": "NEWPO",
            "default": false,
            "timestamp": 1575578382,
            "facility": null
        },
        {
            "id": 551,
            "client": "BARRYR",
            "deptid": "ORIENT",
            "dept": "",
            "billctr": "",
            "manager": "",
            "phone": "",
            "billytd": "0.00",
            "skillcode": "",
            "site": "NEWPO",
            "default": false,
            "timestamp": 1575578382,
            "facility": 24
        },
        {
            "id": 421,
            "client": "ROSEHI",
            "deptid": "ORIENT",
            "dept": "",
            "billctr": "",
            "manager": "",
            "phone": "",
            "billytd": "0.00",
            "skillcode": "",
            "site": "NEWPO",
            "default": false,
            "timestamp": 1575578382,
            "facility": 52
        },
        {
            "id": 448,
            "client": "RRMC1",
            "deptid": "MAIN",
            "dept": "",
            "billctr": "",
            "manager": "",
            "phone": "",
            "billytd": "16779.00",
            "skillcode": "",
            "site": "NEWPO",
            "default": false,
            "timestamp": 1575578382,
            "facility": 58
        }
    ]
}
