import argparse
import configparser
import smtplib
import email.utils
from email.message import EmailMessage


def mail_sender(recipient, host, port, sender, username, password):
    print(f"with love, from {username} to {recipient}")

    # Create the message
    subject = 'With love, from ME to YOU'
    text = '''This is an example test'''
    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = subject
    SENDERNAME = 'Sender Name'
    msg['From'] = email.utils.formataddr((SENDERNAME, sender))
    msg['To'] = recipient

    # Try to send the message.
    try:
        # Open communication and send
        server = smtplib.SMTP(host, port)
        server.ehlo()
        server.starttls()
        # stmplib docs recommend calling ehlo() before & after starttls()
        server.ehlo()
        server.login(username, password)
        server.sendmail(sender, recipient, msg.as_string())
        server.close()
    # Display an error message if something goes wrong.
    except Exception as e:
        print("Error: ", e)
    else:
        print("Email sent!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('email', type=str, help='destination email')
    parser.add_argument('-c', dest='config', type=argparse.
                        FileType('r'),
                        help='config file', default=None)
    args = parser.parse_args()
    if not args.config:
        print('Error, a config file is required')
        parser.print_help()
        exit(1)

    config = configparser.ConfigParser()

    config.read_file(args.config)
    mail_sender(recipient=args.email,
                host=config['DEFAULT']['host'],
                port=config['DEFAULT']['port'],
                sender=config['DEFAULT']['email'],
                username=config['DEFAULT']['username'],
                password=config['DEFAULT']['password'])
