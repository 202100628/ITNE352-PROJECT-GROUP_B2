import socket
import json
import tkinter as tk
from tkinter import messagebox, simpledialog

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432

def transmitRequest(socket_client, request_message):
    socket_client.send(request_message.encode('utf-8'))
    length_response_str = socket_client.recv(10).decode('utf-8').strip()
    length_response = int(length_response_str)
    data_response = b""
    while len(data_response) < length_response:
        part_data = socket_client.recv(length_response - len(data_response))
        data_response += part_data
    return json.loads(data_response.decode('utf-8'))

def searchNewsHeadlines(socket_client):
    search_window = tk.Toplevel(main_window)
    search_window.title("Search News Headlines")

    def search_and_display(query_type, query_params):
        data_news = transmitRequest(socket_client, f'get_news|{query_type}|{json.dumps(query_params)}')
        displayResults(data_news, search_window)

    tk.Button(search_window, text="Search by Keyword", command=lambda: search_and_display('everything', {'q': simpledialog.askstring("Keyword", "Enter keyword:")})).pack(fill=tk.X)
    tk.Button(search_window, text="Search by Category", command=lambda: search_and_display('top-headlines', {'category': simpledialog.askstring("Category", "Enter category:")})).pack(fill=tk.X)
    tk.Button(search_window, text="Search by Country", command=lambda: search_and_display('top-headlines', {'country': simpledialog.askstring("Country", "Enter country code:")})).pack(fill=tk.X)
    tk.Button(search_window, text="List All Headlines", command=lambda: search_and_display('top-headlines', {})).pack(fill=tk.X)
    tk.Button(search_window, text="Back", command=search_window.destroy).pack(fill=tk.X)

def retrieveSourcesList(socket_client):
    sources_window = tk.Toplevel(main_window)
    sources_window.title("List of Sources")

    def search_and_display(query_params):
        data_sources = transmitRequest(socket_client, f'get_news|sources|{json.dumps(query_params)}')
        displaySources(data_sources, sources_window)

    tk.Button(sources_window, text="Search by Category", command=lambda: search_and_display({'category': simpledialog.askstring("Category", "Enter category:")})).pack(fill=tk.X)
    tk.Button(sources_window, text="Search by Country", command=lambda: search_and_display({'country': simpledialog.askstring("Country", "Enter country code:")})).pack(fill=tk.X)
    tk.Button(sources_window, text="Search by Language", command=lambda: search_and_display({'language': simpledialog.askstring("Language", "Enter language code:")})).pack(fill=tk.X)
    tk.Button(sources_window, text="List All Sources", command=lambda: search_and_display({})).pack(fill=tk.X)
    tk.Button(sources_window, text="Back", command=sources_window.destroy).pack(fill=tk.X)

def displayResults(data_news, parent_window):
    results_window = tk.Toplevel(parent_window)
    results_window.title("News Results")
    if data_news['status'] == 'ok':
        for article in data_news['articles']:
            tk.Button(results_window, text=article['title'], command=lambda a=article: show_article_details(a)).pack(fill=tk.X)
    else:
        messagebox.showerror("Error", "Failed to fetch news.")

def show_article_details(article):
    details_window = tk.Toplevel(main_window)
    details_window.title("Article Details")
    tk.Label(details_window, text=f"Title: {article['title']}", wraplength=400).pack()
    tk.Label(details_window, text=f"Description: {article['description']}", wraplength=400).pack()
    tk.Label(details_window, text=f"Source: {article['source']['name']}").pack()
    tk.Label(details_window, text=f"URL: {article['url']}", wraplength=400).pack()

def displaySources(data_sources, parent_window):
    sources_window = tk.Toplevel(parent_window)
    sources_window.title("Sources List")
    if data_sources['status'] == 'ok':
        for source in data_sources['sources']:
            tk.Label(sources_window, text=f"{source['name']} ({source['country']})").pack()
    else:
        messagebox.showerror("Error", "Failed to fetch sources.")

if __name__ == '__main__':
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect((SERVER_HOST, SERVER_PORT))
    
    username_client = simpledialog.askstring("Username", "Enter your name:")
    socket_client.send(username_client.encode('utf-8'))

    main_window = tk.Tk()
    main_window.title("News Search Client")

    tk.Button(main_window, text="Search News Headlines", command=lambda: searchNewsHeadlines(socket_client)).pack(fill=tk.X)
    tk.Button(main_window, text="List News Sources", command=lambda: retrieveSourcesList(socket_client)).pack(fill=tk.X)
    tk.Button(main_window, text="Quit", command=main_window.quit).pack(fill=tk.X)

    main_window.mainloop()
    socket_client.close()
