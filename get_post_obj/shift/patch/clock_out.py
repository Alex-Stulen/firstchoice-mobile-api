# Clock-out shift logic


def ClockOut()

    api_url = 'https://firstchoicenurses.com/api/v1/mobile/obj/shift/<int:pk>/clock-out'

    method = 'PATCH'
    headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH

    patch_fields = {
            "latitude": <type:float>,
            "longitude": <type:float>
            }

    returns = {'shift object. Read `get_shift.py`'}

