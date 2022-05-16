import socket
sock = socket.socket()
try:
    sock.bind(('', 80))
except OSError:
    sock.bind(('', 8080))
sock.listen(5)
conn, addr = sock.accept()
print('Cjnnected', addr)
conn.close()

conn, addr = sock.accept()
print('Connected', addr)
data = conn.recv(8192)
msg = data.decode()
print(msg)

resp = """HTTP/1.1 200 OK
Hello, webworld!"""
conn.send(resp.encode())
conn.close

#http server

import socket
import sys

max_line = 64*1024

class server:
  def __init__(self, host, port, server_name):
    self.host = host
    self.port = port
    self.server_name = server_name

  def server_info(self):
    serv_sock = socket.socket(
      socket.AF_INET,
      socket.SOCK_STREAM,
      proto=0)

    try:
      serv_sock.bind((self._host, self._port))
      serv_sock.listen()

      while True:
        conn, addr = serv_sock.accept()
        try:
          self.serve_client(conn)
        except Exception:
          print('Client serving failed')
    finally:
      serv_sock.close()

  def serve_client(self, conn):
    try:
      request = self.parse_request(conn)
      response = self.handle_request(req)
      self.send_response(conn, resp)
    except ConnectionResetError:
      conn = None
    except Exception as e:
      self.send_error(conn, e)

    if conn:
      conn.close()


  def parse_request(self, conn):
    rfile = conn.makefile('rb')
    method, target, ver = self.parse_request_line(rfile)
    headers = self.parse_headers(rfile)
    return Request(method, target, ver, headers, rfile)


  def parse_headers(self):

    headers = []
    while True:
      line = rfile.readline(max_line + 1)
      if len(line) > max_line:
        raise Exception('Header line is too long')

      if line in (b'\r\n', b'\n', b''):
        # завершаем чтение заголовков
        break

      headers.append(line)
      if len(headers) > max_line:
        raise Exception('Too many headers')
    return headers



if __name__ == '__main__':
  host = sys.argv[1]
  port = int(sys.argv[2])
  name = sys.argv[3]

  serv = server(host, port, name)
  serv.server_info()
  

