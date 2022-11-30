import socket as s, pickle
from client_config import ClientConfig as config

class Constants():
    # Client
    ARGUMENT_ERROR = "Server or Port can not be null:"
    SERVER_CONNECT = "A connection was successfully established with the server:"
    EXIT = "Write *exit* to quit server connection."
    INSERT = "Insert prompt: "
    FINISH = "Image received successfully."

    # Server sincronization
    DISCONNECT = "exit"
    FINISH_IMG = "Image sent successfully."

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
        socket = s.socket(s.AF_INET, s.SOCK_STREAM)
        socket.connect((self.__server, int(self.__port)))
        print(f"{Constants.SERVER_CONNECT} {self.__server}:{self.__port}")

        print(Constants.EXIT) # Print how to exit server.
        while True:
            # User input
            answer = input(Constants.INSERT)

            # Send promt to server
            encode = pickle.dumps(answer)
            socket.send(encode)

            # Disconnect from server
            if (answer == Constants.DISCONNECT):
                data = socket.recv(1024)
                decode = pickle.loads(data)
                if (decode == Constants.DISCONNECT):
                    print("Disconnected from server.")
                    break

            data = socket.recv(8192)
            print(pickle.loads(data))

            continue

            # Receive image from server
            folder = './images/' + answer + ".jpg"
            archive = open(folder,'wb')
            while True:
                data = socket.recv(8192)
                if data.decode('utf-8', 'ignore') == Constants.FINISH_IMG:
                    print(Constants.FINISH, folder)
                    break
                #decode = pickle.loads(data)
                archive.write(data)
            archive.close()

            
            
# Run Client
if __name__=="__main__":
    main = Main()
    main.main()
