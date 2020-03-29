#! python3
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
        address = pyperclip.paste('https://www.google.com/maps/place/' + address)

    webbrowser.open()

except Exception as e:
    logging.error('Error: ' + e)

logging.debug('End of program')