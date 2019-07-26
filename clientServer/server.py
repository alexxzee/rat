import socket
import http.server
import subprocess
from .tools import serverTools as server

def main():
  host = '127.0.0.1'
  port = 1337
  memory = 8000
  msgConnRec = '[LOG] New connection from: '
  msgListener = 'Listen: '
  encode = 'UTF-8'

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((host, port))
  s.listen(1)
  print(msgListener)

  conn, addr = s.accept()

  print(msgConnRec, addr)

  data = conn.recv(memory)

  server.displayData(data)

  openShell = 'cmd /c ' + str(data.decode(encode))

  popen = subprocess.Popen(
    openShell,
    shell=True, 
    stdin=None,
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE)

  (out, err) = popen.communicate()

  conn.send(str(out).encode(encode))

  conn.close()







