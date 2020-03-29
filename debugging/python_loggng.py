'''
debug(lowest)
info
warning
error
critical(highest)
'''
import logging
# logging to a file just pass a parameter 
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s ')
# Disables all logging from critical level to lower since it is highest in level
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial (%s)' %(n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is %s, total is %s' % (i , total))

    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program')