# Filter shifts by hospitals && internaFrom && internalTo without nurse by token
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/facility/shift/filter?hospitals=1,2,3&internalFrom=1233412&internalTo=123123'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH

returns = {'short shift objects. Read `get_shift.py`'}
