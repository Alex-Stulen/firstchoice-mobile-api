# User verification by date of birth

def VerificationByDob():

    api_url = 'https://firstchoicenurses.com/api/v1/mobile/auth/verification-by-dob'
    
    method = 'POST'
    headers = REQUIRED_HEADERS_FOR_TOKEN_AUTH

    post_fields = {
                    'dob': <type: str>, template: '2021-01-01',
                    'last_four_ssn': <type: str>, template: '1234'
                }

    returns = 'Read verification.py'

