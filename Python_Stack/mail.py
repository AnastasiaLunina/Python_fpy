import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:
    """
    Creating SMTP client session objects for mailing
    Accessing Gmail Inbox using Python imaplib module
    """
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def send_email(self, subject, recipients, message, header=None):
        """
        connecting to a server to send an email
        identify ourselves to smtp gmail client
        secure our email with tls encryption
        re-identify ourselves as an encrypted connection
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.login
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = subject
            msg.attach(MIMEText(message))
            server = smtplib.SMTP(self.GMAIL_SMTP, 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.login, self.password)
            server.sendmail(self.login, recipients, msg.as_string())
            server.quit()
        except Exception as exception:
            return f'Failed to send email:{exception}'

    def receive_email(self, header=None):
        try:
            mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
            mail.login(self.login, self.password)
            mail.list()
            mail.select("inbox")
            criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
            result, data = mail.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            latest_email_uid = data[0].split()[-1]
            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email.message_from_string(raw_email)
            mail.logout()
        except Exception as exception:
            return f'Failed to receive email:{exception}'


if __name__ == '__main__':
    recipients = ['some.recipient@gmail.com']

    mail_google = Email('your.email@gmail.com', 'your_password')
    mail_google.send_email("subject", recipients, "message")
    mail_google.receive_email()

