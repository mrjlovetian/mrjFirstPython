import smtplib
from email.mime.text import MIMEText

msg = MIMEText("The body of email is here")

msg['Subject'] = 'An email alert'
msg['From'] = '1520312758@qq.com'
msg['to'] = '409360559@qq.com'

s = smtplib.SMTP('smtp.qq.com')
s.send_message(msg)
s.quit