import base64
import socket
import ssl

pswd = 'universitateatehnicafcimsi151'
user = 'UTM.FCIM.SI151'
MAIL_From = 'MAIL From: <UTM.FCIM.SI151@gmail.com>'.encode() + '\r\n'.encode()
RCPT_To = 'RCPT To: <'

pswd64 = base64.b64encode(bytearray(pswd.encode()))
user64 = base64.b64encode(bytearray(user.encode()))
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = context.wrap_socket(s, server_hostname="www.gmail.com")
ssl_sock.connect(('smtp.gmail.com', 465))

recv = ssl_sock.recv(1024)
recv = recv.decode()
print("Message after connection request:"+recv)

heloCommand = 'EHLO AILZ\r\n'
ssl_sock.send(heloCommand.encode())
recv1 = ssl_sock.recv(1024)
recv1 = recv1.decode()
print("Message after EHLO command:"+recv1)

authMes = 'AUTH LOGIN'.encode() + '\r\n'.encode()
ssl_sock.send(authMes)
recv_auth = ssl_sock.recv(1024)
print(recv_auth.decode())

ssl_sock.send(user64+ '\r\n'.encode())
recv_auth = ssl_sock.recv(1024)
print(recv_auth.decode())

ssl_sock.send(pswd64+'\r\n'.encode())
recv_auth =ssl_sock.recv(1024)
print(recv_auth.decode())

ssl_sock.send(MAIL_From)
recv_auth = ssl_sock.recv(1024)
print(recv_auth.decode())

raw_to = input('Receiver: ')
RCPT_To = RCPT_To.encode() + raw_to.encode() + '>'.encode() + '\r\n'.encode()

ssl_sock.send(RCPT_To)
recv_auth = ssl_sock.recv(1024)
print((recv_auth.decode()))

ssl_sock.send('DATA\r\n'.encode())
recv_auth = ssl_sock.recv(1024)
print(recv_auth.decode())

raw_mes = input('Your Message: ')
mess = raw_mes + '\r\n.\r\n'

ssl_sock.send(mess.encode())
recv_auth = ssl_sock.recv(1024)
print(recv_auth.decode())