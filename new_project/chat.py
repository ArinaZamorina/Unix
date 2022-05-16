import time, socket, sys

socket = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)

port = 9090

socket.bind((host_name, port))
logging.info('Binding is completed')

print('IP: ', ip)

user_name = input('Name: ')

socket.listen(1)
conn, add = socket.accept()

print('Received connection from', add[0])

user = (conn.recv(1024)).decode()
print(f'{user} has connected')

conn.send(name.encode())

while True:
    message = input('User:')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(f'{user} : {message}')
    
