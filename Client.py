# Client.py:
# ```python
import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_client(self):
        self.client_socket.connect((self.host, self.port))
        print("Connected to server on {}:{}".format(self.host, self.port))
        while True:
            command = input("Enter a command: ")
            self.client_socket.send(command.encode())
            # receive command execution from server
            execution = self.client_socket.recv(1024).decode()
            print("Command execution: {}".format(execution))


# class Client:
#     def __init__(self, host, port):
#         self.host = host
#         self.port = port
#         self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     def start_client(self):
#         self.client_socket.connect((self.host, self.port))
#         print("Connected to server on {}:{}".format(self.host, self.port))
#         while True:
#             command = input("Enter a command or type 'rank' to check your rank: ")
#             if command == 'rank':
#                 self.check_rank()
#             else:
#                 self.client_socket.send(command.encode())
#                 # receive command execution from server
#                 execution = self.client_socket.recv(1024).decode()
#                 print("Command execution: {}".format(execution))

#     def check_rank(self):
#         # send message to server asking for rank
#         self.client_socket.send("rank".encode())
#         # receive rank from server
#         rank = self.client_socket.recv(1024).decode()
#         print("Your rank is: {}".format(rank))