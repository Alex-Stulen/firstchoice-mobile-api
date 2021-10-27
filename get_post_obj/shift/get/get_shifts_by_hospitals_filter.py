# Get shifts by hospitals filter

def GetShiftsByHospitalsFilter():
    
    api_url = 'https://firstchoicenurses.com/api/v1/mobile/obj/shift/filter'
    
    method = 'GET'
    headers = REQUIRE_HEADERS_FOR_TOKEN_AUTH

    get_fields = {
                'hospitals_id': <type: list>,
                'internal_from': <type: int>,
                'internal_to': <type: int>
            }

    returns {'shift objects. Read `get_shift.py`'}

