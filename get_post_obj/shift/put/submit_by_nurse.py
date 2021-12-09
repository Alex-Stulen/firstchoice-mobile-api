# Nurse submit shift

def NurseSubmitShift():

	api_url = 'https://firstchoicenurses.com/api/v1/mobile/obj/shift/<int:pk>/submit-by-nurse' # <int:pk> - primary key for shift
	method = 'PUT'
	headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
	post_fields = {
                'submitted_nurse_shift_files': <type: list. Optional>,
                'fields for update shift'...
            }
            # Note:
            	'submitted_nurse_shift_files' - cannot be empty. Can contain one file path.
            	'submitted_nurse_shift_files' - is an array with file paths.
            	example:
            		{
            			'submitted_nurse_shift_files': ['/uploads/test/folder/test_icon.png']
            			 OR
            			'submitted_nurse_shift_files': ['/uploads/test/folder/file1.pdf', '/uploads/test/folder/file2.pdf', ...]
            		}

	returns = {
		'shift data. Read `get_shift.py`'
	}

