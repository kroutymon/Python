import smtplib

user = "trollmanhd@gmx.net"
pwd = "pw"
mail_text = "hallooooooooooooooo"
subject = "test"

mail_from = "trollman@gmx.net"
rcpt_to = "karafiat84@gmail.com"
#%s (insert) \n ("enter")
data = "From:%s\nTo:%s?nSubject:%s\n\n%" % (mail_from, rcpt_to, subject, mail_text)

#tls:587 Standardport für SMTP-Übermittlung
server = smtplib.SMTP("secure.emailsrvr.com:587")
server.starttls()
server.login(user, pwd)
server.sendmail(mail_from, rcpt_to, data)
server.quit()