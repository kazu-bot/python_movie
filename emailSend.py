#emailを送ってみるコード
from email import message
import smtplib

smtp_host = 'smtp.gmail.com'
smtp_port = 587
from_email = 'xxxx2dx@gmail.com'
#from_email = config.from_email
to_email = 'xxxx2dx@gmail.com'
#to_email = config.to_email
username = 'xxxx2dx@gmail.com'
#username = config.username
password = 'fcmkuhpfdufuuxih'
#password = config.password

msg = message.EmailMessage()
msg.set_content('Test email')
msg['subject'] = 'Test Emal sub'
msg['From'] = from_email
msg['To'] = to_email

server = smtplib.SMTP(smtp_host,smtp_port)
server.ehlo()
server.starttls()
#もう一回会話E Hello
server.ehlo()
server.login(username,password)
server.send_message(msg)
server.quit()