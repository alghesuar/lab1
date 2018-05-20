import socket
import ssl
pswd = 'universitateatehnicafcimsi151'
user = 'UTM.FCIM.SI151'
MAIL_From = 'MAIL From: <UTM.FCIM.SI151@gmail.com>'.encode() + '\r\n'.encode()
RCPT_To = 'RCPT To: <'

context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = context.wrap_socket(s, server_hostname="www.gmail.com")
ssl_sock.connect(('imap.gmail.com', 995))

recv = ssl_sock.recv(1024)
print(recv)

ssl_sock.send('USER UTM.FCIM.SI151\r\n'.encode())
recv = ssl_sock.recv(1024)
print(recv)

ssl_sock.send('PASS universitateatehnicafcimsi151\r\n'.encode())
recv = ssl_sock.recv(1024)
print(recv)

ssl_sock.send('LIST\r\n'.encode())
recv = ssl_sock.recv(1024)
print(recv.decode())

ssl_sock.send('RETR 5\r\n'.encode())
recv = ssl_sock.recv(1024)
print(recv.decode())

recv = ssl_sock.recv(1024)
print(recv.decode())