import urllib2
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login('j2menupotpie@gmail.com', 'j2potpie')

j2Menu = "http://hf-food.austin.utexas.edu/foodpro/menuSamp2.asp?locationNum=12&locationName=Jester+2nd+Floor+Dining&sName=University+of+Texas+%2D+Division+of+Housing+%26+Food+Service&naFlag=1"

header = {'User-Agent': 'Mozilla/5.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

req = urllib2.Request(j2Menu, headers=header)

page = urllib2.urlopen(req)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page, "html.parser")
thing = soup.find_all(string="Vegetable Pot Pie")
if thing:
    msg = MIMEMultipart()

    subscriberList = ['sparikh98@gmail.com', 'sparikh29@gmail.com', "alanzeng17@gmail.com", "akhil.amin.98@gmail.com"]

    msg['From'] = 'j2menupotpie@gmail.com'
    msg['To'] = ",".join(subscriberList)
    msg['Subject'] = "Vegetable pot pie today at J2"

    s.sendmail('j2menupotpie@gmail.com', subscriberList, msg.as_string())

s.quit()
