import socket

#clase para simular un servidor
host = "127.0.0.1"
port = 6666

class chatserver:

#constructor crea e inicializa un socket y lo mantiene en escucha

    def __init__(self):
        self.soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Socket Created")

        self.soquete.bind((host, port))
        print ("socket bind complete")
        self.soquete.listen(1)
        print ("socket now listening")

#método que manda mensajes al cliente.

    def run(self):
        while 1:
            conn, addr = self.soquete.accept()
            try:
                print('conexion con {}.'.format(addr))
                conn.send("server: Hello client".encode('UTF-8'))
                while True:
                     datos = conn.recv(4096)
                     if datos:
                         print('recibido: {}'.format(datos.decode('utf-8')))
                     else:
                         print("prueba")
                         break
            finally:
                conn.close()

S = chatserver()
S = S.run()
