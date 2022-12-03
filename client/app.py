import socket as s, pickle, os
from client_config import ClientConfig as config

class Constants():
    # Client
    ARGUMENT_ERROR = "Server or Port can not be null:"
    SERVER_CONNECT = "A connection was successfully established with the server:"
    SERVER_CONNECT_ERROR = "Cannot connect the computer to the server:"
    EXIT = "Write *exit* to quit server connection."
    INSERT = "Insert prompt: "
    FINISH = "Image received successfully in folder: "
    EMPTY = "Can't send empty messages. Try again."

    # Server sincronization
    DISCONNECT = "exit"

class Main():

    # Constructor
    def __init__(self):
        self.__server = config.SERVER
        self.__port = config.PORT

    def main(self):

        if (self.__server != ""):
            if (self.__port != ""):
                self.__client()
                return

        print(Constants.ARGUMENT_ERROR, self.__server)

    def __client(self):
        # Connect to server
        socket = s.socket(s.AF_INET, s.SOCK_STREAM)

        try:
            socket.connect((self.__server, int(self.__port)))
        except:
            print(f"{Constants.SERVER_CONNECT_ERROR} {self.__server}:{self.__port}")
            return

        print(f"{Constants.SERVER_CONNECT} {self.__server}:{self.__port}")

        print(Constants.EXIT) # Print how to exit server.
        while True:
            # User input
            answer = input(Constants.INSERT)

            if not answer or answer.isspace():
                print(Constants.EMPTY)
                continue

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

            # Get image from server
            self.__getImage(socket, answer)
            

    def __getImage(self, socket, prompt):
        """
            Receive image from server.
        """
        folder_exists = os.path.exists(config.FOLDER_IMG)
        
        if not folder_exists:
            os.makedirs(config.FOLDER_IMG)

        folder = f'{config.FOLDER_IMG}{prompt[:200]}.png'
        archive = open(folder,'wb')

        while True:
            data = socket.recv(8192)

            if data.decode('utf-8', "ignore").endswith(Constants.DISCONNECT):
                print(Constants.FINISH, folder)
                break

            archive.write(data)

        archive.close()


# Run Client
if __name__=="__main__":
    main = Main()
    main.main()
