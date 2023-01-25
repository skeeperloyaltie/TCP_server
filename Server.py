import threading

class Server:
    def __init__(self, host, port, max_clients):
        self.host = host
        self.port = port
        self.max_clients = max_clients
        self.clients = []
        self.ranks = {}
        self.lock = threading.Lock() # create a lock to synchronize access to shared resources
        
    def handle_client(self, client_socket):
        while True:
            try:
                command = client_socket.recv(1024).decode()
                command_rank = self.ranks[client_socket]
                print("Received command '{}' from client with rank {}".format(command, command_rank))
                # acquire the lock before accessing the shared resources
                self.lock.acquire()
                for other_client in self.clients:
                    other_client_rank = self.ranks[other_client]
                    if other_client_rank > command_rank:
                        other_client.send(command.encode())
                        print("Sent command '{}' to client with rank {}".format(command, other_client_rank))
                    else:
                        print("Rejected command '{}' from client with rank {} to client with rank {}".format(command, command_rank, other_client_rank))
                # release the lock after accessing the shared resources
                self.lock.release()
            except:
                self.clients.remove(client_socket)
                rank = self.ranks.pop(client_socket)
                print("Client with rank {} disconnected".format(rank))
                self.promote_clients(rank)
                break
                
    def promote_clients(self, rank):
        # acquire the lock before accessing the shared resources
        self.lock.acquire()
        for client in self.clients:
            if self.ranks[client] > rank:
                self.ranks[client] -= 1
                print("Promoted client with rank {} to rank {}".format(self.ranks[client]+1, self.ranks[client]))
        # release the lock after accessing the shared resources
        self.lock.release()
