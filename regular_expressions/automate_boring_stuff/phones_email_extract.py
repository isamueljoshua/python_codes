#! python3

import re, pyperclip

# Create a regex for phone numbers
# phoneRegex = re.compile(r'''
# # 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

# (((\d\d\d)|(\(\d\d\d\)))?        # area code (optional)
# (\s|-)       # first seperator
# \d\d\d        # first 3 digits
# -        # seperator
# \d\d\d\d        # last 4 digits
# ((ext(\.)?\s|x)         # extension word part(optional)
#  (\d{2,5})))       # extension number part(optional)
# ''', re.VERBOSE)

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# TODO: Create a regex for email addresses
emailRegex = re.compile(r'''
# example some.+thing@(\d{2,5})?.com

[a-zA-Z0-9_.+]+        # name part(don't need to escape . _ or + inside sqr brackets)
@        # @ symbol
[a-zA-Z0-9_.+]+        # domain name part

''', re.VERBOSE)
# TODO: Get the text off the clipboard
text = pyperclip.paste()

# TODO: Extract the email/phone from this text
# this findall returns a list of tuples for each match, and each tuple has several strings in it,
# one string for each group, simple way to solve this is put everything inside a very large group
# then group 0 is going to cover the entire matched text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
        allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)
print(extractedEmail)

# TODO: Copy the extracted email/phone to the clipboard