import socket
import threading
import requests
import json
import os

API_KEY_NEWS = 'b9221b54e43c4adeaef44036df9c021e'
# print (API_KEY_NEWS)
URL_BASE = 'https://newsapi.org/v2/'
ADDRESS_HOST = '127.0.0.1'
NUMBER_PORT = 65432

def fetchNews(api_endpoint, query_params):
  query_params['apiKey'] = API_KEY_NEWS
  api_response = requests.get(URL_BASE + api_endpoint, params=query_params)
  if api_response.status_code == 200:
    return api_response.json()
  else:
    return {'status': 'error', 'message': 'Unable to fetch data'}

def storeFormattedData(project_id, username_client, option_type, content_data):
  file_path = f"{project_id}{username_client}{option_type}.json"
  with open(file_path, 'w') as file:
    json.dump(content_data, file)
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
