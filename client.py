import socket
import json

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432

def transmitRequest(socket_client, request_message):
  socket_client.send(request_message.encode('utf-8'))
  length_response_str = socket_client.recv(10).decode('utf-8').strip()
  print(f"Received response length string: '{length_response_str}'")
  length_response = int(length_response_str)
  print(f"Received response length: {length_response}")
  data_response = b""
  while len(data_response) < length_response:
    part_data = socket_client.recv(length_response - len(data_response))
    data_response += part_data
  return json.loads(data_response.decode('utf-8'))

def main():
  username_client = input("Enter your name: ")
  socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  socket_client.connect((SERVER_HOST, SERVER_PORT))
  socket_client.send(username_client.encode('utf-8'))

  while True:
    pass

  socket_client.close()

if __name__ == '__main__':
  main()
