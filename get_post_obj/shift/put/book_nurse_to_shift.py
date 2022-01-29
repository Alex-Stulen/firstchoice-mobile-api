# Book nurse to shift
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/shift/<int:shift_pk>/booked'
method = 'PUT'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
put_fields = 'special put fields are not needed'

returns = 'returns shift short info'
