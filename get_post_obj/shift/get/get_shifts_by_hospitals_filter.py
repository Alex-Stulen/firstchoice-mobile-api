# Get shifts by hospitals filter

def GetShiftsByHospitalsFilter():
    
    api_url = 'https://firstchoicenurses.com/api/v1/mobile/obj/shift/filter?hospitals=1,2,3&internalFrom=123123&internalTo=123123'
    
    method = 'GET'
    headers = REQUIRE_HEADERS_FOR_TOKEN_AUTH

    returns {'shift objects. Read `get_shift.py`'}

