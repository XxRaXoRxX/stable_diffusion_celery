import socket, pickle
from client_config import ClientConfig as config

class Constants():
        ARGUMENT_ERROR = "Server or Port can not be null:"
        SERVER_CONNECT = "A connection was successfully established with the server:"
        EXIT = "Write *exit* to quit server connection."
        INSERT = "Insert prompt: "
        DISCONNECT = "exit"

class Main():

    # Constructor
    def __init__(self):
        self.__server = config.SERVER
        self.__port = config.PORT

    def main(self):

        if (self.__server != ""):
            if (self.__port != ""):
                self.client()
                return

        print(Constants.ARGUMENT_ERROR, self.__server)

    def client(self):
        # Connect to server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.__server, int(self.__port)))
        print(f"{Constants.SERVER_CONNECT} {self.__server}:{self.__port}")

        print(Constants.EXIT) # Print how to exit server.
        while True:
            # User input
            answer = input(Constants.INSERT)

            # Send promt to server
            encode = pickle.dumps(answer)
            s.send(encode)

            # Receive image from server
            recv = s.recv(1024)
            decode = pickle.loads(recv)
            print(decode)

            # Disconnect from server
            if (decode == Constants.DISCONNECT):
                print("Disconnected from server.")
                break
            
# Run Client
if __name__=="__main__":
    main = Main()
    main.main()
