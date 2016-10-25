# coding=utf-8
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = raw_input('From: ')
password = raw_input('Password: ')
to_addr = raw_input('To: ')
smtp_server = raw_input('SMTP server: ')


# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python爱好者<%s>' % to_addr)
msg['To'] = _format_addr(u'管理员<%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候...', 'utf-8').encode()

msg.attach(MIMEText(('send with file...', 'plain', 'utf-8'))

with open('C:/work/test.png', 'rb') as f:
    mime = MIMEBase('image', 'png', filename='test.png')
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '<0>')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()