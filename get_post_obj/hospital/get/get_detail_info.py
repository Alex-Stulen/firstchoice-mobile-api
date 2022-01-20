# Get detail info about special hospital
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/hospital/<int:hospital_id>/detail-info'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = 'special get fields are not needed'

returns = { # returns error 404 if hospital does not exist
	    "id": 14,
	    "username": null,
	    "email": null,
	    "password": null,
	    "comments": null,
	    "timestamp": 1575578382,
	    "shortcode": "NANSPT",
	    "name": "Nansemond Pointe Rehab & Healthcare",
	    "attention": null,
	    "address": "200 W. Constance Rd.",
	    "address2": null,
	    "city": "Suffolk",
	    "st": "VA",
	    "zipcode": "23434",
	    "contact": "Gennette - Staff Developme",
	    "phone": "+17575398744",
	    "phone1": "+17575396128",
	    "phone2": "",
	    "phone3": "",
	    "vfemail": "Admin- Mel Appelle\r\nDON-\r\n",
	    "vfcomments": " go I -64 towards suffolk -   downtown suffolk exit, follow a little bit down to you see McDonalds pass McDonalds  2nd driveway on your right W. Constance ( sign back a little )",
	    "show_aging": true,
	    "facility_type": "Facility",
	    "account_representative": "",
	    "invoice_method": "C",
	    "early_pay_discount_rate": "0.0000",
	    "early_pay_due": 0,
	    "invoice_due": 35,
	    "invoice_late_rate": "1.5000",
	    "invoice_late_fee": "0.00",
	    "factoring_agent": "ADVANCE",
	    "auto_add_travel": false,
	    "round_invoice_hours": false,
	    "site": "NEWPO",
	    "covid_vaccine": false,
	    "notes": null,
	    "covid_exemption": false,
	    "notes_for_covid_exemption": null
	}
