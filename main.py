from email.message import EmailMessage
import ssl
import smtplib
import requests
from datetime import date
from bs4 import BeautifulSoup
url="https://docs.google.com/spreadsheets/d/1yVRZmrs4Tt5SXWqZ15xbOaJcp1q-N4kCPHUm3tN6kKs/edit?usp=drivesdk"
def ttt(rawtime):
  r = rawtime.split("-")
  datee=["มกราคม","กุมภาพันธ์","มีนาคม","เมษายน","พฤษภาคม","มิถุนายน","กรกฎาคม","สิงหาคม","กันยายน","ตุลาคม","พฤศจิกายน","ธันวาคม"]
  return f"วันที่ {int(r[2])} เดือน {datee[int(r[1])-1]} ปี {r[0]}"
r=requests.get(url)
soup=BeautifulSoup(r.text, "html.parser")
v=soup.text
k=((v.split(","))[2:-13])
print(k)
work=[]
warning =[]
for i in range(0,len(k),11):
  print(i)
  work.append(k[i:i+11])
print(work)
morningmail=[f"สวัสดีตอนเช้าครับ คุณมีงานดังต่อไปนี้ที่ยังค้างคา"]
for j,val in enumerate(work):
  if int(val[10])==100:
    continue
  t=["<"]
  for i in range((int(int(val[10])/10))):
    t.append("=")
  t.append(f"{val[10]}%")
  for i in range(10-((int(int(val[10])/10)))):
    t.append("-")
  t.append(">")
  if int(val[8])==1:
    warning.append(f" 💥 {val[1]} จากวิชา {val[2]} ทำไปแล้ว {''.join(t)} รายละเอียดงาน {val[7]}")
  morningmail.append(f"◼ สำคัญ {val[5]} เหลือเวลาอีก {val[8]} วัน ' {val[1]}' จากวิชา {val[2]} สั่งวันที่ {val[3]} และ กำหนดส่งวันที่ {val[4]} ทำไปแล้ว {''.join(t)} อ่านต่อได้ที่ {val[7]}")
morningmail.append(f"รวมเป็น {len(morningmail)-1} งาน ขอบคุณครับ")
print(morningmail)
print(warning)

pwd = "pttq izsc qslj unns"
sender="why1spr.socute@gmail.com"
reciever = "kittiphasa29@gmail.com"
subject = f"งานประจำ {ttt(str(date.today()))}"
body= "\n".join(morningmail)
em = EmailMessage()
em['From']= sender
em['To'] = reciever
em['Subject']= subject
em.set_content(body)
con = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=con) as smtp:
  smtp.login(sender,pwd)
  smtp.sendmail(sender,reciever,em.as_string())

emp = EmailMessage()
emp['From']= sender
emp['To'] = reciever
emp['Subject']= f"ส่งพรุ่งนี้!!! {ttt(str(date.today()))}"
emp.set_content("\n".join(warning))
conp = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=conp) as smtp:
  smtp.login(sender,pwd)
  smtp.sendmail(sender,reciever,emp.as_string())

