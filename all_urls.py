

'/api/v1/mobile/auth/login'                        		# Login url. Read `auth/login.py`
'/api/v1/mobile/auth/verification'                 		# Verification url. Read `auth/verification.py`
'/api/v1/mobile/auth/verification-by-dob'          		# Verification by user date of birth
'/api/v1/mobile/auth/logout'                       		# Logout url. Read `auth/logout.py`

'/api/mobile/obj/facility/admin-detail-info'			     # Get current Facility Admin detail info
'/api/mobile/obj/facility/all-admin-hospitals'			     # Get all hospitals ids for current facility admin
'/api/mobile/obj/facility/shift/filter'				     # Filter shifts by hospitals and internal_from && internal_to datetime 									       without nurse by token
'/api/mobile/obj/facility/<int:facility_id>/get-future-shifts'       # Get all futures shifts for special facility
'/api/mobile/obj/facility/shift/<int:shift_id>/set-as_certified'     # Set special shift as certified
'/api/mobile/obj/facility/shift/<int:shift_id>/set-as-rejected'	     # Set special shift as rejected
'/api/mobile/obj/facility/shift/get-all-by-status?status=...'        # Get all shifts by special status. Ex: .../get-all-by-status?status=pending
'/api/mobile/obj/facility/shift/<int:facility_id>/get-all-by-status?status=...' # Get all shifts by special status for special hospital
'/api/mobile/obj/facility/shift/create'						# Create shift record
'/api/mobile/obj/facility/hospital/<int:hospital_id>/detail-info'               # Get detail info about special hospital
'/api/mobile/obj/facility/nurse/<int:nurse_id>/assign-to-shift'			# Assign nurse to shift
'/api/mobile/obj/facility/dept/get-all-departments'				# Get all departments
'/api/mobile/obj/facility/dept/<int:hospital_id>/get-all-departments'		# Get all departments for special hospital
'/api/mobile/obj/facility/hospital/<int:hospital_id>/get-all-classifications'	# Get all classifications for special hospital 

'/api/v1/mobile/obj/nurse'                            # Get current Nurse detail info. Read `get_post_obj/nurse/get_nurse.py`
'/api/v1/mobile/obj/nurse/<int:nurse_id>/detail-info' # Get special Nurse detail info
'/api/v1/mobile/obj/nurse/search'		      # Search nurse by fname or lname fields
'/api/v1/mobile/nurse/add-credential'		      # Creane new Nurse credential entry.
'/api/v1/mobile/nurse/update-credential/<int:id>'  # Update Nurse Credential
'/api/v1/movibe/nurse/get-all-credentials'	   # Get all Nurse Credentials.
'/api/v1/mobile/nurse/add-education'		   # Create new Nurse education entry.
'/api/v1/mobile/nurse/update-education/<int:id>'   # Update Nurse Education
'/api/v1/mobile/nurse/get-all-educations' 	   # Get all Nurse Educations.
'/api/v1/mobile/obj/nurse/profile/update'	   # Updated fields for current nurse
'/api/v1/mobile/obj/nurse/profile/change-password' # Updated Nurse password
'/api/v1/mobile/obj/nurse/assigned-shifts'         # Get current Nurse assigned shifts. Read `get_post_obj/nurse/get_assigned_shifts.py`
'/api/v1/mobile/obj/nurse/assign-to-shift'	   # Set nurse to special shift
'/api/v1/mobile/obj/nurse/cancel-assign-to-shift'  # Remove nurse from special shift
'/api/v1/mobile/obj/nurse/past-shifts'		   # Get all past shifts for nurse
'/api/v1/mobile/obj/nurse/certified-shifts'        # Get current Nurse certified shifts. Read `get_post_obj/nurse/get_certified_shifts.py`
'/api/v1/mobile/obj/nurse/all-booked-shifts'	   # Get all booked Shifts for Nurse
'/api/v1/mobile/obj/nurse/get-all-core-credentials' # Get all Core Credentials records for Nurse
'/api/v1/mobile/obj/nurse/core-credential/identifying-documents/create/<int:core_cred_id>' # Create Identifying Document instance
'/api/v1/mobile/obj/nurse/core-credential/identifying-documents/<int:document_id>/remove-file' # Remove file for Identifying Document instance
'/api/v1/mobile/obj/nurse/core-credential/identifying-documents/<int:document_id>/delete' # Delete Identifying Document instance
'/api/v1/mobile/obj/nurse/core-credential/update/<int:core_cred_id>' # Update Core Credential for Nurse
'/api/v1/mobile/obj/nurse/core-credential/get-info/<int:core_cred_id>' # Get info about Nurse Core Credential
'/api/v1/mobile/obj/nurse/core-credential/remove-file' # Remove file for Core Credentials. Only for: ('PPD', 'BLS', 'Urine Drug Screen', 'Flu Vaccine')
'/api/v1/mobile/obj/nurse/core-credential/sub-core/remove-file' # Remove file for Core Credentials. Only for: ('Professional License')

'/api/v1/mobile/obj/shift/<int:pk>/clock-in'       # Indicates the fields to shift when the nurse started the shift
'/api/v1/mobile/obj/shift/<int:pk>/clock-out'      # Indicates the fields to shift when the nurse stop the shift
'/api/v1/mobile/obj/shift/<pk>/update'             # Endpoint for update shift
'/api/v1/mobile/obj/shift/<int:shift_pk>/booked>'  # Booke nurse to shift
'/api/v1/mobile/obj/shift/filter'                  # Filter shifts by hospitals and internal_from && internal_to datetime

'/api/v1/mobile/obj/hospital/list'                 # Returns all hospitals
'/api/v1/mobile/obj/hospital/<int:pk>/all-shifts'  # Returns all shifts for special hospital (<int:pk>) - primary key for hospital

'/api/v1/mobile/upload-files'  			   # Saves downloaded files to the system in global upload folder.
'/api/v1/mobile/upload-files/<path:folder_paths>'  # Saves downloaded files to the system in a specific folder.

