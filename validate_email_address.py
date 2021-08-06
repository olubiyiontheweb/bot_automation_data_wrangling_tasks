import argparse
import re


def validate_email_address(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return True
    return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', help='Email address to validate')
    args = parser.parse_args()
    print(
        f'This value {args.email} is an email address: {validate_email_address(args.email)}')
