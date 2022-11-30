import socket, pickle, sys
from celery import Celery
import base64
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from server_config import ServerConfig as config
# setting path
sys.path.append('../')
from worker.tasks import GetImage


class Constants():
    START = "Server Started in:"
    CONNECT = "is connected."
    DISCONNECT = "is disconnected."
    DISCONNECT_CLIENT = "exit"
    CONFIG = "Can configure server in server_config.py"
    SENDING_IMAGE = "Sending image to client:"
    FINISH = "Image sent successfully."
    

class Main():
    def main(self):
        self.Server()

    # Server runner
    def handle(self, socket, address):
        # Show Address.
        print(f"|| {address[0]}:{address[1]}", Constants.CONNECT, "||")

        while True:
            # Get prompt from client
            data = socket.recv(1024)
            decode = pickle.loads(data)
            print(f"<< {address[0]}:{address[1]} prompt:", decode, ">>")

            # Disconnect client.
            if (decode == "exit"):
                encode = pickle.dumps(Constants.DISCONNECT_CLIENT)
                socket.send(encode)
                print(f"|| {address[0]}:{address[1]}", Constants.DISCONNECT, "||")
                break

            # Send image to client
            print("<<", Constants.SENDING_IMAGE, f" {address[0]}:{address[1]} >>")

            img = open("./images/test_image.jpg", 'rb')
            while True:
                print("reading readline")
                send = img.read(8192)
                print("sending")
                if not send:
                    print("<<", Constants.FINISH, f" {address[0]}:{address[1]} >>")
                    socket.send(Constants.FINISH.encode('utf-8'))
                    break
                #encode = pickle.dumps(send)
                socket.send(send)

    # Server Starter
    def Server(self):
        address = (config.HOST, int(config.PORT))
        executor = ThreadPoolExecutor(max_workers = config.THREAD)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #... tenemos un pool "executor", y un socket que se llama "s"
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(address)
            s.listen(config.MAX_CLIENTS)

            print(Constants.START, f"{config.HOST}:{config.PORT}")
            print(Constants.CONFIG)
            
            while True:
                s2, addr = s.accept()
                result = executor.submit(self.handle, s2, addr)
                #s2.close()

# Runear server.
if __name__ == '__main__':
    main = Main()
    main.main()