# IMAP - Internet Message Access Protocol
# IMAP specifies how to communicate with your email provider server to retrieve emails that were sent to your email address

# python comes with a module called imaplib, but we will be using imapclient and pyzmail

import imapclient
import pyzmail

# Note: if the above does not work the login to gmail in your browser first, and go to https://www.google.com/settings/security/lesssecureapps and enable it, wait for few minutes and then run again

# domain name for gmail is imap.gmail.com, you can google for your provider's IMAP domain
# ssl is an encryption standard - tells imap client that we want to use ssl encryption
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)

# login with your email ID and password
conn.login('your_mail_id@gmail.com', 'your_gmail_password_here')
# select your mail's inbox with readonly so that you don't accidentally delete a mail
conn.select_folder('INBOX', readonly=True)
# search for mails with a list of strings, returns a list of unique IDs which refers to a particular mail
# new method
# SINCE is the IMAP search key
UIDS = conn.search(b'SINCE 20-Apr-2020')
print(UIDS)
# old method
# UIDS = conn.search(['SINCE 20-Apr-2020'])

# fetch one of the IDs returned
rawMessage = conn.fetch([12041], ['BODY[]', 'FLAGS'])

# use pyzmail to parse the output
message = pyzmail.PyzMessage.factory(rawMessage[12041][b'BODY[]'])

# get's the subject of the mail
print(message.get_subject())

# returns the tuple of ('Mail sender's name', 'their mail address')
print(message.get_address('from'))

# who mail was sent to
print(message.get_address('to'))

# who is in bcc
print(message.get_address('bcc'))

# check if there was a text part in the mail
print(message.text_part)
# check if there was a HTML part in the mail
print(message.html_part)

# to get the actual content of text part
# UTF-8 is an encoding standard, 99 % it is this standard
print(message.text_part.get_payload().decode('UTF-8'))

# to check the encoding standard
print("\nCharset: ",message.text_part.charset)

# returns a tuple containing folders, the name of folder is the 3rd item in that folder
print(conn.list_folders())

# to DELETE emails
# conn.select_folder('INBOX', read_only=False)
# UIDs = conn.search(b'ON 24-AUG-2020')
# print(UIDS)
# # call delete and pass any one or all Uids to delete
# conn.delete_messages([387273])

conn.logout()