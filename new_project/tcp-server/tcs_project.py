#создать простой TCP сервер, который принимает от клиента строку и возвращает ее

sock = socket.socket()
sock.bind((input('Server host: ', ''), input('Server port: ') or 9090))
sock.listen(1)
conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

conn.close()


# создать сокет, подключиться к серверу, послать данные, принять и закрыть
#2
import socket
sock = socket.socket()
sock.connect((input('Host: ' or 'localhost'), input('Port: ' or '9090')))
while True:
    i = input()
    if i != 'exit':
        sock.send(i)
    else:
        break

data = sock.recv(1024)
sock.close()

print(data)




