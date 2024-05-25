import socket
import threading
import requests

ADDRESS_HOST = '127.0.0.1'
NUMBER_PORT = 65432

def processClientRequest(socket_client, address):
  print(f"Accepted connection from {address}")
  try:
    username_client = socket_client.recv(1024).decode('utf-8')
    print(f"Client name: {username_client}")
    while True:
      client_request = socket_client.recv(1024).decode('utf-8')
      if not client_request:
          break
      print(f"Requester: {username_client}, Request: {client_request}")
      if client_request.startswith('get_news'):
          response_message = "Under development! News functionality coming soon."
          response_message = response_message.encode('utf-8')
          socket_client.sendall(response_message)
      else:
          error_message = json.dumps({'status': 'error', 'message': 'Invalid request'}).encode('utf-8')
          socket_client.sendall(error_message)
  except ConnectionResetError:
    pass
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
