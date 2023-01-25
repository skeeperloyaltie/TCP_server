import socket
import threading

class Server:
    def __init__(self, host, port, max_clients):
        self.host = host
        self.port = port
        self.max_clients = max_clients
        self.clients = [] # list to store connected clients
        self.ranks = {} # dictionary to store client ranks (key: client, value: rank)

    def start_server(self):
        # create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(self.max_clients)
        print("Server started on {}:{}".format(self.host, self.port))

        # continuously listen for new clients
        while True:
            client_socket, client_address = server_socket.accept()
            if len(self.clients) < self.max_clients:
                # assign rank to new client based on first-come-first-serve
                rank = len(self.clients)
                self.ranks[client_socket] = rank
                self.clients.append(client_socket)
                print("Client {} connected with rank {}".format(client_address, rank))
                # start a new thread to handle communication with this client
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_thread.start()
            else:
                client_socket.close()
                print("Rejected connection from {}: maximum clients reached".format(client_address))

    def handle_client(self, client_socket):
        while True:
            try:
                # receive command from client
                command = client_socket.recv(1024).decode()
                command_rank = self.ranks[client_socket]
                print("Received command '{}' from client with rank {}".format(command, command_rank))
                # distribute command to other clients
                for other_client in self.clients:
                    other_client_rank = self.ranks[other_client]
                    if other_client_rank > command_rank:
                        other_client.send(command.encode())
                        print("Sent command '{}' to client with rank {}".format(command, other_client_rank))
                    else:
                        print("Rejected command '{}' from client with rank {} to client with rank {}".format(command, command_rank, other_client_rank))
            except:
                # if an error occurs, the client has disconnected
                self.clients.remove(client_socket)
                rank = self.ranks.pop(client_socket)
                print("Client with rank {} disconnected".format(rank))
                self.promote_clients(rank)
                break

    def promote_clients(self, rank):
        """
        This method is called when a client disconnects, and it re-adjusts the ranks of the remaining clients
        to fill the gap left by the disconnected client. It promotes clients with a rank higher than the
        disconnected client's rank.
        :param rank: The rank of the disconnected client
        """
        for client in self.clients:
            if self.ranks[client] > rank:
                self.ranks[client] -= 1
                print("Promoted client with rank {} to rank {}".format(self.ranks[client]+1, self.ranks[client]))