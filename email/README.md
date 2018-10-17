
```python
#!/usr/local/python34/bin/python3
#-*- encoding: utf-8 -*-

import os
import sys
import smtplib
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

mailInfo = {
    "from": "support@seliencepuppet.com",
    "to": sys.argv[1],
    "hostname": "smtp.qq.com",
    "username": "support@seliencepuppet.com",
    "password": "1234567890",
    "mailsubject": sys.argv[2],
    "mailtext": sys.argv[3],
    "mailencoding": "utf-8"
}

if __name__ == '__main__':
    smtp = SMTP_SSL(mailInfo["hostname"])
    smtp.set_debuglevel(1)
    smtp.ehlo(mailInfo["hostname"])
    smtp.login(mailInfo["username"],mailInfo["password"])
    msg = MIMEText(mailInfo["mailtext"],"text",mailInfo["mailencoding"])
    msg["Subject"] = Header(mailInfo["mailsubject"],mailInfo["mailencoding"])
    msg["from"] = mailInfo["from"]
    msg["to"] = mailInfo["to"]
    smtp.sendmail(mailInfo["from"], mailInfo["to"], msg.as_string())
    smtp.quit()
```
