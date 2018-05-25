import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


smtp_email = 'yamenmarquez@gmail.com'
smtp_password = 'Lgoogleenon100184'
recipients_mail = 'kpisthatmatter@gmail.com'
files = 'SAV CLG SHFCO 12X5500131.pdf'
  
msg = MIMEMultipart()
msg['From'] = smtp_email
msg['To'] = recipients_mail
msg['Subject'] = 'Pruba de envío de correo con adjunto desde python'
 
body = "YOUR MESSAGE HERE"

msg.attach(MIMEText(body, 'plain'))

filename =  files
attachment = open(files, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(smtp_email, smtp_password)

text = msg.as_string()

server.sendmail(smtp_email, recipients_mail, text)
server.quit()
print('Correo enviado')