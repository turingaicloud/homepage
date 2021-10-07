import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
import sys

subject = "TACC October Newsletter"
file = open(sys.argv[1]).readlines()

list_trs = "trs-smart-city-team@lists.ust.hk"
list_tacc = "tacc-contact@lists.ust.hk"
list_users = "tacc-users@lists.ust.hk"
to_addrs = [list_tacc]

content = " ".join(file)
addr = "kxuar@connect.ust.hk"
password = "Matters826!!"

msg = EmailMessage()
msg.add_header('Content-Type','text/html')
msg.set_payload(content)
msg['Subject'] = subject
msg['From'] = "Kaiqiang Xu <%s>" % addr
msg['To'] = ",".join(to_addrs)

srv = smtplib.SMTP('smtp.office365.com', 587)
srv.starttls()
srv.login(addr, password)
srv.send_message(msg)
srv.quit()