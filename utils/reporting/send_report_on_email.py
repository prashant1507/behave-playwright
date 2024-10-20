import configparser
import smtplib
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from helpers.constants.framework_constants import FrameworkConstants as Fc
from utils.helper_utils import read_file

subject = "Test Report"
body = "Please find the attached file."

details = configparser.ConfigParser()
details.read(Fc.details_file)

def send_email_with_attachment(file_path, logger):
    global server
    msg = MIMEMultipart()

    msg['From'] = details.get("email", "sender_email")
    msg['To'] = details.get("email", "receiver_email")
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))
    filename = os.path.basename(file_path)
    attachment = open(file_path, 'rb')

    mime_base = MIMEBase('application', 'octet-stream')
    mime_base.set_payload(attachment.read())
    encoders.encode_base64(mime_base)
    mime_base.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(mime_base)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(details.get("email", "sender_email"), details.get("email", "token"))
        server.sendmail(details.get("email", "sender_email"), details.get("email", "receiver_email"), msg.as_string())
        logger.info("Email sent successfully.")
    except Exception as e:
        logger.info(f"Failed to send email: {e}")
    finally:
        attachment.close()
        server.quit()


def send_report(logger, file_path):
    if details.getboolean("email", "send_report_on_email"):
        logger.info("Sending Report on Email")
        send_email_with_attachment(file_path, logger)
