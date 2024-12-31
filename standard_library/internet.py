# 有许多模块可用于访问互联网和处理互联网协议。
# 其中两个最简单的 urllib.request 用于从URL检索数据，以及 smtplib 用于发送邮件:
from urllib.request import urlopen
with urlopen('https://www.python.org/') as response:
    for line in response:
        line = line.decode()
        if line.startswith('<title>'):
            print(line[7:-8])

import smtplib
from email.mime.text import MIMEText
msg = MIMEText('Python is awesome!')
msg['Subject'] = 'Test message'
msg['From'] = 'your@email'
msg['To'] = 'target@email'
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()