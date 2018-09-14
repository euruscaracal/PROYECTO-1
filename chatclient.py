import socket

host = "127.0.0.1"
port = 6666

#clase que simula el cliente
class chatclient:

    def __init__(self):

        self.soquete = socket.socket()
        self.soquete.connect((host, port))

    def run(self):
        datos = self.soquete.recv(4096)
        print (datos.decode('utf-8'))

        while True:
          message = input("envia un mensaje: ")
          self.soquete.send(message.encode('utf-8'))

          if message == "quit":
            print("bye")
            self.soquete.close()
            break

S = chatclient()
S = S.run()
