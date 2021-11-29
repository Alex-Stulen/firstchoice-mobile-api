# Uploading files to the system

'https://dev.firstchoicenurses.com/api/v1/mobile/upload-files'
 OR
'https://dev.firstchoicenurses.com/api/v1/mobile/upload-files/<path:folder_paths>'
The first link will save the files to the global downloads folder
The second link will save the files to a specific folder at the specified path.
	Example:
		if you want to save files to a folder in a special path ('/<global folder for uploads:indicated automatically>/test/folder')
		in folder 'test/folder'.
		you must send a request to '/api/v1/mobile/upload-files/test/folder'
		
method = 'POST'
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

returns = 'Read `get_shift.py`'

"""===================================================================="""
