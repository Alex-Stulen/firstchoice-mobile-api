

'/api/v1/mobile/auth/login'                       # Login url. Read `auth/login.py`
'/api/v1/mobile/auth/verification'                # Verification url. Read `auth/verification.py`
'/api/v1/mobile/auth/verification-by-dob'         # Verification by user date of birth
'/api/v1/mobile/auth/logout'                      # Logout url. Read `auth/logout.py`

'/api/v1/mobile/obj/nurse'                        # Get current Nurse detail info. Read `get_post_obj/nurse/get_nurse.py`
'/api/v1/mobile/obj/nurse/assigned-shifts'        # Get current Nurse assigned shifts. Read `get_post_obj/nurse/get_assigned_shifts.py`
'/api/v1/mobile/obj/nurse/assign-to-shift'	  # Set nurse to special shift
'/api/v1/mobile/obj/nurse/cancel-assign-to-shift' # Remove nurse from special shift
'/api/v1/mobile/obj/nurse/past-shifts'		  # Get all past shifts for nurse
'/api/v1/mobile/obj/nurse/certified-shifts'       # Get current Nurse certified shifts. Read `get_post_obj/nurse/get_certified_shifts.py`

'/api/v1/mobile/obj/shift/<int:pk>/clock-in'      # Indicates the fields to shift when the nurse started the shift
'/api/v1/mobile/obj/shift/<int:pk>/clock-out'     # Indicates the fields to shift when the nurse stop the shift
'/api/v1/mobile/obj/shift/<pk>/update'            # Endpoint for update shift
'/api/v1/mobile/obj/shift/filter'                 # Filter shifts by hospitals and internal_from && internal_to datetime

'/api/v1/mobile/obj/hospital/list'                # Returns all hospitals
'/api/v1/mobile/obj/hospital/<int:pk>/all-shifts' # Returns all shifts for special hospital (<int:pk>) - primary key for hospital

