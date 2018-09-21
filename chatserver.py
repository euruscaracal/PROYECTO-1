import socket
import threading
import pickle
import sys
from threading import Thread

#clase para simular un servidor

class chatserver:
    ip = "0.0.0.0"
    port = 1234
#constructor crea e inicializa un socket y lo mantiene en escucha

    def __init__(self):

        self.soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Socket Created")
        self.soquete.bind((self.ip, self.port))
        print ("socket bind complete")
        self.soquete.listen()
        print ("socket now listening")
        self.clientes = []


    def conexiones(self):
        self.hilo = threading.Thread(target=self.recibirmensaje)
        self.hilo.daemon = True
        self.hilo.start()

    def establece(self):
        try:
            while True:
                print("Waiting for conexion...")
                m = input("Recibo mensajes: ")
                if m == "DISCONNECT":
                    self.soquete.close()
                    sys.exit()
                    break
        except:
            pass

    def send(self, mensaje, cliente):
         for c in self.clientes:
             if c != cliente:
                 self.c.send(mensaje)
             else:
                 self.clientes.remove(c)

    def run(self):
        while True:
            conn, addr = self.soquete.accept()
            self.soquete.setblocking(False)
            self.clientes.append(conn)
            hilo = threading.Thread(target=self.recibirmensaje(conn))
            hilo.daemon = True
            hilo.start()


    def recibirmensaje(self,conn):
        while True:
             datos = conn.recv(1024)
             if datos:
                 self.send(datos,conn)
             else:
                 print("Te has desconectado. ¡Vuelve pronto!")
                 conn.close()
                 break



S = chatserver()
S.run()
