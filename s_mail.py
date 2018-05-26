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


smtp_email = 'yamenmarquez@gmail.com'
smtp_password = 'Lgoogleenon100184'
mail_recipients = ['kpisthatmatter@gmail.com', 'maritzahechavarriaduran@gmail.com']
files_to_attach_path = ".coas_por_enviar" +os.sep
coas_dir_path = "COAs" + os.sep

files_to_attach = os.listdir(files_to_attach_path)

# for f in files_to_attach:
#     print(f)

send_email(smtp_email, smtp_password, mail_recipients, files_to_attach, files_to_attach_path)

current_path = os.getcwd() + os.sep

for file in files_to_attach:
    origin = current_path + files_to_attach_path + file
    destination = current_path + coas_dir_path + file

    if os.path.exists(origin):
        shutil.move(origin, destination)
        print('El archivo ha sido movido a', origin)
    else:
        print('No existe archivo para mover')