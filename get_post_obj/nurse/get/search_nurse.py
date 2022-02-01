# Search Nurse by fname or lname fields
'https://dev.firstchoicenurses.com/api/v1/mobile/obj/nurse/search?text=Alex+Test&page=1'
method = 'GET'
headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
get_fields = {
	'text': <type: string. Required>,
	'page': <type: int. Optional. Default equal 1>
}


returns = {
    "total_pages": <type: int>,
    "page_size": <type: int>,
    "current_page": <type: int>,
    "data": <type: array. Array with nurses objects>
}
