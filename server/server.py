import socket, pickle, sys, os, base64
from celery import Celery
from datetime import date
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from server_config import ServerConfig as config
# setting path
sys.path.append('../worker')
from tasks import GetImage

class Constants():
    # Server
    START = "Server Started in:"
    CONNECT = "is connected."
    DISCONNECT = "is disconnected."
    CONFIG = "Can configure server in server_config.py"
    SENDING_IMAGE = "Sending image to client..."
    FINISH = "Image sent successfully."
    REDIS = "Sending prompt to redis..."
    SAVE_IMAGE = "Saving image in server..."
    ERROR = "Error to create image."

    # Client sincronization
    DISCONNECT_CLIENT = "exit"

class Main():
    def main(self):
        self.__server()

    # Server runner
    def __handle(self, socket, address):
        # Show Address.
        self.__printMsg(Constants.CONNECT, address, True)

        while True:
            # Get prompt from client
            prompt = self.__getSocketData(socket)

            self.__printMsg("prompt: " + prompt, address)

            # Disconnect client.
            if (prompt == "exit"):
                self.__sendSocketData(socket, Constants.DISCONNECT_CLIENT)
                self.__printMsg(Constants.DISCONNECT, address, True)
                break

            # Send message to redis.
            self.__printMsg(Constants.REDIS, address)
            image = self.__sendRedis(prompt)

            # Save Image
            self.__printMsg(Constants.SAVE_IMAGE, address)
            self.__saveImage(image, prompt)
            
            self.__sendSocketData(socket, "Recibido")

            # Send image to client
            # if (result != None):
            #     self.__printMsg(Constants.SENDING_IMAGE, address)
            #     img = open(f"{config.FOLDER_IMG}/{date.today()}{decode}.jpg", 'rb')
            #     while True:
            #         print("reading readline")
            #         send = img.read(8192)
            #         print("sending")
            #         if not send:
            #             self.__printMsg(Constants.FINISH, address)
            #             socket.send(Constants.FINISH.encode('utf-8'))
            #             break
            #         #encode = pickle.dumps(send)
            #         socket.send(send)
            # else:
            #     self.__sendSocketData(socket, Constants.ERROR)

    # Server Starter
    def __server(self):
        """
        Start server.
        """
        address = (config.HOST, int(config.PORT))
        executor = ThreadPoolExecutor(max_workers = config.THREAD)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Config Server
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(address)
            s.listen(config.MAX_CLIENTS)

            # Print Server Config
            print(Constants.START, f"{config.HOST}:{config.PORT}")
            print(Constants.CONFIG)
            
            # Start Server
            while True:
                s2, addr = s.accept()
                result = executor.submit(self.__handle, s2, addr)
                #s2.close()

    def __getSocketData(self, socket):
        """
        Handle data send from client.

        Args:
            - socket: Socket to get data.
        """
        data = socket.recv(1024)
        return pickle.loads(data)

    def __sendSocketData(self, socket, data):
        """
        Handle data send from server.

        Args:
            - socket: Socket to send data.
            - data : data to encode and send.
        """
        encode = pickle.dumps(data)
        socket.send(encode)

    def __printMsg(self, msg, address, connection: bool = False):
        """
        Print message.

        Args:
            - msg (str): Message to print.
            - address (str): Address to print.
            - connection (bool): If is a connection message.
        """
        if (connection):
            print(f"<< {address[0]}:{address[1]}", msg, ">>")
        else:
            print(f"|| {address[0]}:{address[1]}", msg, "||")

    def __sendRedis(self, prompt):
        """
        Send prompt to redis.

        Args:
            - prompt (str): Prompt to send.
        """
        result = GetImage.delay(prompt)
        return result.get()

    def __saveImage(self, image, prompt):
        """
        Save image in server.

        Args:
            - prompt (str): Prompt to send.
            - image (str): Image encoded in Celery.
            - prompt (str): Prompt to create image.
        """

        print("save image")
        # Decode image
        image = image.encode()
        image = base64.b64decode(image)

        print("image decoded")
        # Save image
        folder = str(prompt).replace(' ', '_')
        folder = f'./images/{folder}/{date.today()}.png'
        os.makedirs(os.path.dirname(folder), exist_ok=True)
        with open(folder,'wb') as f:
            f.write(image)

# Runear server.
if __name__ == '__main__':
    main = Main()
    main.main()