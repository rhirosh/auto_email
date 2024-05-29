import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

def send_email(subject, email_to, email_from, csv_path, filename, body, cc_emails=None, smtp_server=None, smtp_port=None, username=None, password=None):
    msg = MIMEMultipart()
    msg["From"] = email_from
    msg['To'] = ", ".join(email_to)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, 'plain'))  # 'plain' indicates plain text
    fileToSend = csv_path
    ctype, encoding = mimetypes.guess_type(fileToSend)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    if maintype == "text":
        fp = open(fileToSend, encoding="utf-8")
        # Note: we should handle calculating the charset
        attachment = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "image":
        fp = open(fileToSend, "rb")
        attachment = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "audio":
        fp = open(fileToSend, "rb")
        attachment = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(fileToSend, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename=filename)
    msg.attach(attachment)

    server = smtplib.SMTP('relay.brasilis.com.br:25')

    server.sendmail(email_from, email_to, msg.as_string())
    server.quit()