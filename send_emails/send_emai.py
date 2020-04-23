import smtplib

# domain name is smtp.gmail.com and port is 587
# ports are part of internet address you are sending data to, some providers can change this port as well
# for more info: https://automatetheboringstuff.com/chapter16/
conn = smtplib.SMTP('smtp.gmail.com', 587)

print(type(conn))
print(conn)

# print(conn.ehlo())

# connecting to the server
conn.ehlo()

# start the tls encryption, so that when  we send across a password it will be encrypted
conn.starttls()

# login with your email id and password
conn.login('your_mail_id@gmail.com', 'your_gmail_passwrd')

# send mail with from_address, to_address, and content with Subject: 
# the return value is going to be the emails it failed to send to as a dict
fro = 'your_mail_id@gmail.com'
to = 'to_mail_id@gmail.com'
conn.sendmail(fro , to, 'Subject: Hi friend....\n\nDear friendooo,\ntest automat mail. \n\n-Sam')

# Note: if the above does not work the login to gmail in your browser first, and go to https://www.google.com/settings/security/lesssecureapps and enable it, wait for few minutes and then run again, 
# doing the above works for me,
# if the above also does not work, then refer: https://stackoverflow.com/a/27515833/9197808


# there is also an option to set app specific passwords, search google for google application specific passwords
# we can set passwords for maybe python, phone or TV that logs in to your account
# Gmail usually limits sending mails via this method to almost 150 per day
# If you want to mail 100s of mails, look into a commercial email provider
conn.quit()