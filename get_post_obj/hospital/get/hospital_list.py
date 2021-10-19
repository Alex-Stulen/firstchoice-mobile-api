# Get Hospital list


def GetHospitalList():
    
    api_url = 'https://firstchoicenurses.com/api/v1/mobile/obj/hospital/list'

    method = 'GET'
    headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH

    get_fields = 'special get fields are not needed'

    returns {'list with hospital objects'}

