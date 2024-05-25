import socket
import threading
import requests  

ADDRESS_HOST = '127.0.0.1'
NUMBER_PORT = 65432

def processClientRequest(socket_client, address):
  print(f"Accepted connection from {address}")
  try:

  except ConnectionResetError:

  finally:
    print(f"Client disconnected")
    socket_client.close()

def initializeServer():
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind((ADDRESS_HOST, NUMBER_PORT))
  server_socket.listen(5)
  print(f'Server listening on {ADDRESS_HOST}:{NUMBER_PORT}')

  while True:
    socket_client, address = server_socket.accept()
    client_thread = threading.Thread(target=processClientRequest, args=(socket_client, address))
    client_thread.start()

if __name__ == '__main__':
  initializeServer()
