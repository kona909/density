import re
import density

def test_email_regex():
    """ Tests the regex used to filter Oauth applicants """
    cases = [
        ('nsb2142@columbia.edu', True),
        ('nsb2142@columbia.eduABC', False),
        ('@@nsb2142@columbia.edu', False),
        ('jae@cs.columbia.edu', True),
        ('nsb2142@barnard.edu', True),
        ('nsb2142@yale.edu', False),
    ]

    for email, match in cases:
        assert bool(re.match(density.CU_EMAIL_REGEX, email)) == match
