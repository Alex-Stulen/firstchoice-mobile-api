# Get all shifts by special Hospital


def GetAllShiftsBySpecialHospital():

    api_url = 'https://firstchoicenurses.com/api/v1/mobile/obj/hospital/<int:pk>/all-shifts'
    method = 'GET'
    headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH

    get_fields = {
                "pk": "<type: int> - primary key for special hospital"
            }

    returns = {'list with shifts objects for special hospital. Read `get_shift.py`'}

