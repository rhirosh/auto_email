import smtplib
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText


def send_email_v2(subject, email_to, email_from, csv_buffer, filename, body, cc_emails=None, smtp_server=None,
                  smtp_port=None, username=None, password=None):
    msg = MIMEMultipart()
    msg["From"] = email_from
    msg['To'] = ", ".join(email_to)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, 'plain'))  # 'plain' indicates plain text
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(csv_buffer.getvalue())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment", filename=filename)
    msg.attach(part)
    server = smtplib.SMTP('relay.brasilis.com.br:25')
    server.sendmail(email_from, email_to, msg.as_string())
    server.quit()
