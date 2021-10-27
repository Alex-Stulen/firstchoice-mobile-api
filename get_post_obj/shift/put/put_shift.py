# Update Shift

def UpdateShift():
    
    api_url = 'https://firstchoicenurses.com/api/v1/mobile/obj/shift/<int:pk>/update'
    
    method = 'PUT'
    headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH

    put_fields { 'any fields for shift. For example:',

                'classification': 'lololo',
                'comments': 'some comment',
                'cancelled': true
            }

    returns = {'shift object. Read `get_shift.py`'}

