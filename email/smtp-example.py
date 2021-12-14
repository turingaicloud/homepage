import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
import sys

subject = "New AI Computing Cloud Platform for HKUST" # email Title
file = open(sys.argv[1]).readlines()

list_trs_faculty = "trs-smart-city-faculty@lists.ust.hk"
list_trs_student = "trs-smart-city-team@lists.ust.hk"
list_tacc = "tacc-contact@lists.ust.hk"
list_users = "tacc-users@lists.ust.hk"
test_addr = "andyxukq@gmail.com"

to_addrs = [test_addr] # send-to

content = " ".join(file)
smtp_server = "smtp.cse.ust.hk"
from_addr = "kxuar@cse.ust.hk" # from addr
username = "kxuar" # login handle
password = "" # passoword

msg = EmailMessage()
msg.add_header('Content-Type','text/html')
msg.set_payload(content)
msg['Subject'] = subject
msg['From'] = "TACC <%s>" % from_addr
msg['To'] = ",".join(to_addrs)

srv = smtplib.SMTP(smtp_server, 587)
srv.starttls()
srv.login(username, password)
srv.send_message(msg)
srv.quit()
