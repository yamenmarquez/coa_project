import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from files_manipulation import files_names_read_from_dir

smtp_server = 'smtp.gmail.com' # Servidor smtp que se usará si no se provee ningun otro
smtp_port = 587 # Puerto de conexión al servidor smtp que se usara si no se provee ningun otro

# Variables de prueba para testear el script
from_email = 'yamenmarquez@gmail.com'
from_email_password = 'Lgoogleenon100184'
to_emails = ['kpisthatmatter@gmail.com', 'maritzahechavarriaduran@gmail.com']
files_to_attach_path = "../.coas_por_enviar"+os.sep


def send_email(smtp_server, smtp_port, from_email, from_email_password, to_emails, files_to_attach_path):
    """Envia correo a multiples destinatarios y con multiples adjuntos ubicados en una carpeta conocida

    Argumentos:
    smtp_server -- Servidor smtp desde el que se enviarán los correos
    smtp_port -- Puerto de conexión al servidor smtp
    from_email -- Dirección de correo desde la que se enviarán los correos
    from_email_password -- Password del correo
    to_emails -- Lista con los correos a los destinatarios
    files_to_attach_path -- Path de la carpeta donde se encuantra los archivos a adjuntar
    """
    files_to_attach = files_names_read_from_dir(files_to_attach_path) # Lista con el nombre de los archivos a adjuntar

    msg = MIMEMultipart()
    msg['To'] = ', '.join(to_emails)
    msg['From'] = from_email
    msg['Subject'] = "COAs Quala"

    body = MIMEText('COAs adjuntados.', 'html', 'utf-8')  
    msg.attach(body)  # add message body (text or html)

    for f in files_to_attach:  # add files to the message
        file_path = os.path.join(files_to_attach_path, f)
        attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt")
        attachment.add_header('Content-Disposition','attachment', filename=f)
        msg.attach(attachment)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, from_email_password)
    server.sendmail(msg['From'], to_emails, msg.as_string())
    print('Correo enviado exitosamente')
    server.close()

send_email(smtp_server, smtp_port, from_email, from_email_password, to_emails, files_to_attach_path) # Línea para probar la ejecuión correcta de este script