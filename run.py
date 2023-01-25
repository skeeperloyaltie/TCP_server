import threading
from Server import Server
from Client import Client

if __name__ == '__main__':
    # create a server instance
    server = Server('localhost', 12345, 3)
    # start the server in a new thread
    server_thread = threading.Thread(target=server.start_server)
    server_thread.start()
    # create a client instance
    client = Client('localhost', 12345)
    # start the client
    client.start_client()

