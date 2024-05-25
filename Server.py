import socket
import threading

ADDRESS_HOST = '127.0.0.1'
NUMBER_PORT = 65432

def initializeServer():
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind((ADDRESS_HOST, NUMBER_PORT))
  server_socket.listen(5)
  print(f'Server listening on {ADDRESS_HOST}:{NUMBER_PORT}')

  while True:

if __name__ == '__main__':
  initializeServer()
