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

def printT6(e5):
 e5.wait()
 e5.clear()
 print('This is thread nr.6')
 e5.set()
 
event1 = threading.Event()
event2 = threading.Event()
event3 = threading.Event()
event4 = threading.Event()
event5 = threading.Event()

t1 = threading.Thread(target=printT1, args=(event1,))
t2 = threading.Thread(target=printT2, args=(event1, event2))
t3 = threading.Thread(target=printT3, args=(event2, event3))
t4 = threading.Thread(target=printT4, args=(event3, event4))
t5 = threading.Thread(target=printT5, args=(event4, event5))
t6 = threading.Thread(target=printT6, args=(event5,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
