import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host ='smtp.qq.com'
mail_user ="1064318630"
mail_pass ='*********'

sender ='1064318630@qq.com'
receivers =['1064318630@qq.com']

message =MIMEText('Python','plain','utf-8')
message['From'] =Header("hello world",'utf-8')
message['To'] =Header("GoodBye",'utf-8')

subject ='python try'
message['Subject'] =Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL()
    smtpObj.connect(mail_host,465)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print"success"
except smtplib.SMTPException:
    print"Error:"

