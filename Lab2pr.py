import threading
def printT1(e):
 e.clear()
 print('This is thread nr.1')
 e.set()
 
def printT2(e, e2):
 e.wait()
 e2.clear()
 print('This is thread nr.2')
 e2.set()
 
def printT3(e2, e3):
 e2.wait()
 e3.clear()
 print('This is thread nr.3')
 e3.set()
 
def printT4(e3, e4):
 e3.wait()
 e4.clear()
 print('This is thread nr.4')
 e4.set()
 
def printT5(e4, e5):
 e4.wait()
 e5.clear()
 print('This is thread nr.5')
 e5.set()

def printT6(e5, e6):
 e5.wait()
 e6.clear()
 print('This is thread nr.6')
 e6.set()

def printT7(e6, e7):
 e6.wait()
 e7.clear()
 print('This is thread nr.7')
 e7.set()

def printT8(e7, e8):
 e7.wait()
 e8.clear()
 print('This is thread nr.8')
 e8.set()

def printT9(e8):
 e8.wait()
 e8.clear()
 print('This is thread nr.9')
 e8.set()

event1 = threading.Event()
event2 = threading.Event()
event3 = threading.Event()
event4 = threading.Event()
event5 = threading.Event()
event6 = threading.Event()
event7 = threading.Event()
event8 = threading.Event()

t1 = threading.Thread(target=printT1, args=(event1, ))
t2 = threading.Thread(target=printT2, args=(event1, event2))
t3 = threading.Thread(target=printT3, args=(event2, event3))
t4 = threading.Thread(target=printT4, args=(event3, event4))
t5 = threading.Thread(target=printT5, args=(event4, event5))
t6 = threading.Thread(target=printT6, args=(event5, event6))
t7 = threading.Thread(target=printT7, args=(event6, event7))
t8 = threading.Thread(target=printT8, args=(event7, event8))
t9 = threading.Thread(target=printT9, args=(event8, ))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()