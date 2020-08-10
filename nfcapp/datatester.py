#import sqlite3
import mysql.connector
from email.message import EmailMessage
import smtplib
from datetime import datetime

def sendemail(subject,body,email):
    msg = EmailMessage()
    msg['From'] = '"NFC Club" <nfclub56@gmail.com>'
    msg['To'] = email
    msg['Subject'] = subject
    msg.set_content(body)
    smtplibObj = smtplib.SMTP('smtp.gmail.com',587)
    smtplibObj.ehlo()
    smtplibObj.starttls()
    smtplibObj.login("nfclub56@gmail.com", "Red@1234")

    smtplibObj.send_message(msg)
    smtplibObj.quit()

date = datetime.now()
y = date.year
m = date.month
d = date.day

if m<10:
    m = "0" + str(m)
if d<10:
    d = "0" + str(d)

day = str(y) + "-" + str(m) + "-" + str(d)

#conn = sqlite3.connect('C:\\Users\\PSSRE\\projects\\nfcproject\\db.sqlite3')
conn = mysql.connector.connect(
  host="nofapclub.mysql.pythonanywhere-services.com",
  user="nofapclub",
  password="Red@1234",
  database = "nofapclub$nfcdatabase"
)

email_list = []
mycursor = conn.cursor()
mycursor.execute("SELECT * FROM auth_user")

results = mycursor.fetchall()
for row in results:
    print(row)
    print('1',row[1])
    print('2: ',row[2],' 3:',row[3],' 4: ',row[4],' 5: ',row[5],' 6: ',row[6])
    print(row[7])
    email_list.append(str(row[7]))
mycursor.execute("SELECT * FROM nfcapp_quote_list")
qlist = mycursor.fetchall()
#qlist = conn.execute("SELECT * FROM nfcapp_quote_list")

for row in qlist:
    print(row[1])
    print(row[2])
    if day == str(row[1]):
        print('yes found')
        tday = str(row[1])
        quote = row[2]
        print(quote)
        break




conn.close()
subject = "Daily Quote"
body = "Hi, \n\n" + quote + "\n\n" + "Thanks"
print(email_list)

for i in email_list:

    try:

        sendemail(subject,body,i)
        print('email sent')
    except:
        pass





