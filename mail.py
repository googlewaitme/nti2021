import smtplib 
from email.mime.text import MIMEText
from email.header  import Header


def send_mail(dest_email, text):
    login = 'tom.picks@yandex.ru'
    password = 'TDH5x4az'
    msg = MIMEText(text, 'plain', 'utf-8')
    msg['Subject'] = Header('Это хедер', 'utf-8')
    msg['From'] = login
    msg['To'] = dest_email
    server = smtplib.SMTP_SSL('smtp.yandex.com')
    server.ehlo(login)
    server.login(login, password)
    server.auth_plain()
    server.sendmail(msg['From'], dest_email, msg.as_string())
    server.quit()
