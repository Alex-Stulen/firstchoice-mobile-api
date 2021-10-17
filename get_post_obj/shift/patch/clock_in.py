# Clock-in shift logic


def ClockIn():
    
    api_url = 'https://firstchoicenurses.com/api/v1/mobile/shift/<int:pk>/clock-in'

    method = 'PATCH'
    headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH

    patch_fields = {
            "latitude": <type:float>,
            "longitude": <type:float>
            }

    returns = {'shift object. Read `get_shift.py`'}

