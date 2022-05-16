#создать простой TCP сервер, который принимает от клиента строку и возвращает ее

import socket
import logging

sock = socket.socket()
sock.bind((input('Server host: ', ''), input('Server port: ') or 9090))
logging.info('Прослушивание порта')
sock.listen(1)
logging.info('Подключение')
conn, addr = sock.accept()
logging.info('Приём данных')
while True:
    data = conn.recv(1024)
    if not data:
        break
    logging.info('Отправка данных')
    conn.send(data.upper())

conn.close()


# создать сокет, подключиться к серверу, послать данные, принять и закрыть
#2
import socket
sock = socket.socket()
logging.info('Подключение')
sock.connect((input('Host: ' or 'localhost'), input('Port: ' or '9090')))
while True:
    i = input()
    if i != 'exit':
        logging.info('Отправление данных')
        sock.send(i)
    else:
        break

data = sock.recv(1024)
logging.info('Остановка сервера')
sock.close()

print(data)




