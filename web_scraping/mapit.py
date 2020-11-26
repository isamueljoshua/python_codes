#! python3
# coding: utf-8

__author__ = ["Samuel Joshua"]

# Source + explanation for the whole program: https://automatetheboringstuff.com/chapter11/
# Source running python with bat file and using win key + r https://automatetheboringstuff.com/appendixb/
# the above header is also important to run the script with windows + r
# to successfully run this scrip first install with -- py -m pip install pyperclip
import webbrowser, sys, pyperclip

import logging
# logging to a file just pass a parameter 
logging.basicConfig(filename='mapit_logs.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s ')
# Disables all logging from critical level to lower since it is highest in level
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')

try:
    sys.argv # ['mapit.py', '870', 'Valencia', 'St.]

    # check if command line arguments were passed
    if len(sys.argv) > 1:
        # ['mapit.py', '870', 'Valencia', 'St.] -> '870 Valencia St.'
        address = ' '.join(sys.argv[1:])

    else:
        # https://www.google.com/maps/place/870+Valencia+St,+San+Francisco,+CA+94110 works, also
        # https://www.google.com/maps/place/870 Valencia St, San+Francisco
        # so in general our logic must be https://www.google.com/maps/place/<ADDRESS>
        address = pyperclip.paste()

    webbrowser.open('https://www.google.com/maps/place/' + address)

except Exception as e:
    print(e)
    logging.error('Error: ')

logging.debug('End of program')