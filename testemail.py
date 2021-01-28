import smtplib
import sqlite3 as sqlite

conn = sqlite.connect('test.db')

cur = conn.cursor()

sqlstr1 = 'SELECT email FROM email'

email_list = list()
for row in cur.execute(sqlstr1):
    email_list.append(row)

sqlstr2 = 'SELECT first_name FROM email'
name_list = list()

for row2 in cur.execute():
	name_list.append(row2)
	
cur.close()

for i in range(len(email_list)):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.ehlo()
    s.login("", "")
    message = name_list[i] + "-" + "Did you get my mail"
    s.sendmail("Write the EMAIL ID", email_list[i], message)
    s.quit()
