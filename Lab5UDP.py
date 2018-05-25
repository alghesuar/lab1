import socket
from threading import Thread
import sys

UDP_IP = "255.255.255.255"  # Adresa QuickChat

UDP_PORT = 8167  # portul QuickChat

user = input("Your name: ")

login = '4' + user + '\0' + '#Main' + '\0' + '00'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((UDP_IP, UDP_PORT))  # conectarea la server
sock.send(login.encode())  # transmiterea mesajului de conectare


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("192.168.0.1", 80))
    return s.getsockname()[0]


IP = get_ip_address()

print(IP)


def listen():
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock1.bind((IP, 8167))
    while 1:
        message = sock1.recv(100)
        print(message)


t = Thread(target=listen)
t.start()

while 1:
    msg = input(" ")
    if msg == "Quit":
        message = '5' + user + '\0' + '#Main' + '\0' + '0'
        sock.send(bytearray(message.encode()))

        sock.close()
        sys.quit()
    message = '2#Main' + '\0' + user + '\0' + msg + '\0'
    sock.send(bytearray(message.encode()))