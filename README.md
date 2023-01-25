### TCP Server and Client
- This program creates a TCP server that can accept and hold a maximum of N clients (where N is configurable). These clients are assigned ranks based on first-come-first-serve, i.e whoever connects first receives the next available high rank. Ranks are from 0–N, 0 being the highest rank.

```Server.py```
- The server.py file contains the Server class that creates the server and manages the clients. It has the following methods:

    - init(self, host, port, max_clients): This is the constructor that initializes the server with the given host, port, and maximum number of clients.
    - start_server(self): This method starts the server and continuously listens for new clients.
    - handle_client(self, client_socket): This method handles the communication with a client. It receives commands from the client and distributes them among the other clients.
    - promote_clients(self, rank): This method is called when a client disconnects. It re-adjusts the ranks of the remaining clients to fill the gap left by the disconnected client.

```Client.py```
- The client.py file contains the Client class that creates the client and connects it to the server. It has the following methods:

    - init(self, host, port): This is the constructor that initializes the client with the given host and port.
    - start_client(self): This method starts the client and connects it to the server. It then continuously receives commands from the user and sends them to the server.

```Run.py```
- The run.py file is the main file that runs the program. It creates an instance of the Server class and starts it in a new thread. Then it creates an instance of the Client class and starts it.
How to use
- Run the ```server.py``` file using the command python server.py
- Run the ```client.py``` file using the command python client.py
- The client will be prompted to enter a command, which will be sent to the server and distributed among the other clients.
- The client will also receive commands that have been sent by other clients with a higher rank.
If a client disconnects, the server will re-adjust the ranks of the remaining clients to fill the gap.
## Note
- You can run multiple instances of the client.py file to connect multiple clients to the server.
- The maximum number of clients that can be connected to the server can be configured in the run.py file by changing the value of the max_clients parameter in the Server class constructor.
- The commands are simple, the client just prints to the console that command has been executed.
- The host and port can be configured in the run.py file by changing the values of the host and port parameters in the Server and Client class constructors.