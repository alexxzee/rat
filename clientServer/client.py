import socket
from .tools import clientTools as tools

def main():
  host = '127.0.0.1'
  port = 1337
  memory = 8000
  msgDemand = "Commande: "
  encode = 'UTF-8'

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((host, port))

  command = tools.parseCommand(input(msgDemand))

  sock.send(command)

  data = sock.recv(memory)
  sock.close()
  tools.displayData(data)
