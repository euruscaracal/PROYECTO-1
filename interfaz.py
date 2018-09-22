from tkinter import *
from tkinter import ttk



class Aplicacion():
    def __init__(self):
        raiz = Tk() #ventana principal
        raiz.geometry('500x300') #tamaño de ven
        raiz.configure(bg='#ffd361') #color de ven
        raiz.title('さくら')

        ttk.Button(raiz, text='Salir',
                   command=raiz.destroy).pack(side=BOTTOM)
        raiz.mainloop()

    def main():
        mi_app = Aplicacion()
        return 0

    if __name__ == '__main__':
        main()
