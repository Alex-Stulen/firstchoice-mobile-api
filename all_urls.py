

'/api/v1/mobile/auth/login'                  # Login url. Read `auth/login.py`
'/api/v1/mobile/auth/verification'           # Verification url. Read `auth/verification.py`
'/api/v1/mobile/auth/logout'                 # Logout url. Read `auth/logout.py`

'/api/v1/mobile/obj/nurse'                   # Get current Nurse detail info. Read `get_post_obj/nurse/get_nurse.py`
'/api/v1/mobile/obj/nurse/assigned-shifts'   # Get current Nurse assigned shifts. Read `get_post_obj/nurse/get_assigned_shifts.py`
'/api/v1/mobile/obj/nurse/certified-shifts'  # Get current Nurse certified shifts. Read `get_post_obj/nurse/get_certified_shifts.py`

'/api/v1/mobile/obj/shift/<int:pk>/clock-in'    # Indicates the fields to shift when the nurse started the shift
'/api/v1/mobile/obj/shift/<int:pk>/clock-out'   # Indicates the fields to shift when the nurse stop the shift

'/api/v1/mobile/obj/hospital/list'              # Returns all hospitals
'/api/v1/mobile/obj/hospital/<int:pk>/all-shifts' # Returns all shifts for special hospital (<int:pk>) - primary key for hospital
