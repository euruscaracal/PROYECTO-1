import socket
import threading
import pickle
#clase que simula el cliente
class chatclient:

    def __init__(self):
        self.ip = str(input("Enter IP: "))
        self.port = int(input("Enter port: "))
        self.soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soquete.connect((self.ip, self.port))

    def send(self,msj):
        while True:
            self.soquete.send(pickle.dumps(msj))

    def conexiones(self,msj):
        self.hilo = threading.Thread(target=self.send, args=(msj,))
        self.hilo.daemon = True
        self.hilo.start()

    def run(self):

        while True:
          message = input("Envia un mensaje: ")
          #self.soquete.send(pickle.dumps(message))
          if message == "DISCONNECT":
            print("")
            self.soquete.close()
            break
          else:
             self.conexiones(message)
    def x(self):
        while True:
             datos = conn.recv(1024)
             if datos:
                 self.send(datos,conn)


if __name__ == "__main__":
    S = chatclient()
    S.run()
