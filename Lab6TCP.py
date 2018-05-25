#server
import socket

s = socket.socket()
host = 'localhost'
port = 12221
s.bind((host, port))

s.listen(5)
c = None

while True:
   if c is None:
       # Halts
       print ('[Waiting for connection...]')
       c, addr = s.accept()
       print ('Got connection from', addr)
   else:
       # Halts
       print ('[Waiting for response...]')
       print (c.recv(1024))
       q = input("Enter something to this client: ")
       c.send(bytearray(q.encode()))

#client
import socket

s = socket.socket()
host = 'localhost'
port = 12221

s.connect((host, port))
print ('Connected to', host)

while True:
    z = input("Enter something for the server: ")
    s.send(bytearray(z.encode()))
    # Halts
    print ('[Waiting for response...]')
    print (s.recv(1024))