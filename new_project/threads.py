import threading

def proc(n):
    print 'Process', n

p1 = threading.Thread(target=proc, name='t1', args=['1'])
p2 = threading.Thread(target=proc, name='t2', args=['2'])
p1.start()
p2.start()

#class
import threading

class T(threading.Thread):
    def __init__(self, n):
        threading.Thread.__init__(self, name='t'+n)
        self.n = n
    def run(self):
        print 'Process', self.n

p1 = T('1')
p2 = T('2')
p1.start()
p2.start()

#port scanner

import socket
import threading
import datetime

def scanner (ip,port):
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.settimeout(0.5)

    try:
        connect = new_socket.connect((ip,port))
        print(f'Port: {port}, is opened')
        new_socket.close()

    except:
        pass

time = datetime.now()

ip = '8.8.8.8'
for i in range(100):
    result = threading.Thread(target=scanner, args=(ip,i))
    result.start()
end_time = datetime.now()
print('Time:{}'.format(ends-start))

