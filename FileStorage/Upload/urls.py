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


returns = 'Read `get_shift.py`'

"""===================================================================="""
