# does not work on python3
# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('www.py4inf.com', 80))
# mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0 \n\n'.encode())
# while True:
#     data = mysock.recv(512)
#     if ( len(data) < 1 ) :
#         break
#     print (data)
# mysock.close()

# for python3

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

# Code: http://www.py4e.com/code3/socket1.py