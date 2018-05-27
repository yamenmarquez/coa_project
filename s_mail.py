import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

import shutil

def send_email(smtp_email, smtp_password, mail_recipients, files_to_attach, files_to_attach_path):

    msg = MIMEMultipart()
    msg['To'] = ', '.join(mail_recipients)
    msg['From'] = smtp_email
    msg['Subject'] = "COAs Quala"

    body = MIMEText('COAs adjuntados.', 'html', 'utf-8')  
    msg.attach(body)  # add message body (text or html)

    for f in files_to_attach:  # add files to the message
        file_path = os.path.join(files_to_attach_path, f)
        attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt")
        attachment.add_header('Content-Disposition','attachment', filename=f)
        msg.attach(attachment)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(smtp_email, smtp_password)
    server.sendmail(msg['From'], mail_recipients, msg.as_string())
    print('done!')
    server.close()