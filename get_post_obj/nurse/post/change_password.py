# Update Nurse Password

def UpdateNursePassword():

	api_url = 'https://firstchoicenurses.com/api/v1/mobile/obj/nurse/profile/change-password'
	method = 'POST'
	headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH
	post_fields = {
		"old_password": <type: string. Required>,
		"new_password1": <type: string. Required>,
		"new_password2": <type: string. Required>
	}

	returns = {
	    		"status": true
		}
		# Returns Note:
		#	The response body may vary depending on the result of the server.
		# 	Possible status answers (check response body):
		#		400 - Bad request or The query body does not contain an old password or a new password 1 or a new password 2.
		# 			check response body.
		#		404 - Nurse with this token does not exist.
		# 		403 - old_password != current nurse password or new_password1 != new_password2 (check response body).
		#		200 - OK. Password changed successfully
		# 		401 - Bad Auth Token. Check response body.

