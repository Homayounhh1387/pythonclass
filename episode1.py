from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



msg = MIMEMultipart()
MIMEMultipart["from"] = "saeednikbakht928@gmail.com" 
MIMEMultipart["to"] = 
MIMEMultipart["subject"] = 
msg.attach(MIMEText())
with smtplib.SMTP(host="smtp.google.com" port=567) as server:


