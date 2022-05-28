#Programa que muestra la ventana de pago.

#Librería para los elementos de la GUI.
from tkinter import messagebox as MessageBox
import tkinter as tk  	

class payWindow(object):

    def __init__(self, nuevaVentana):	#Constructor.
        self.Ventana = nuevaVentana
        self.crearVentana()	#Llamada al método crearVentana.

    def crearVentana(self):	#Método para crear la ventana.
        self.Ventana.title("Payment")	#Título de la ventana.
        self.Ventana.attributes('-toolwindow', True) #No permite modificar atributos de la ventana.
        self.Ventana.configure(bg="#000")
        self.Ventana.geometry("600x350")	#Tamaño de la ventana.

        #Configuración de renglones y columnas.
        self.Ventana.columnconfigure(1, weight=1)
        self.Ventana.columnconfigure(3, pad=5)
        self.Ventana.rowconfigure(3, weight=1)
        self.Ventana.rowconfigure(5, pad=5)

        #Etiqueta de encabezado.
        encabezado = tk.Label(self.Ventana, 
                            text="Ingresa los datos de tu tarjeta para pagar.", 
                            font="Verdana 12 bold",
                            bg="#000",
                            fg="#00fb33",
                            pady=20,
                            borderwidth=0)
        #Añadiendo el elemento a la ventana.
        encabezado.grid(row = 0, column = 2) 

         #Etiqueta de número de tarjeta.
        numTar = tk.Label(self.Ventana, 
                            text="Número de tarjeta", 
                            font="Verdana 12 bold",
                            bg="#000",
                            fg="#00fb33",
                            pady=20,
                            borderwidth=0)
        #Añadiendo el elemento a la ventana.
        numTar.grid(row = 1, column = 1)
        txtNum = tk.Entry(self.Ventana,width=50)
        txtNum.grid(row = 1 , column = 2)

         #Etiqueta de nombre completo.
        nombre = tk.Label(self.Ventana, 
                            text="Nombre completo", 
                            font="Verdana 12 bold",
                            bg="#000",
                            fg="#00fb33",
                            pady=20,
                            borderwidth=0)
        #Añadiendo el elemento a la ventana.
        nombre.grid(row = 2, column = 1)
        txtNombre = tk.Entry(self.Ventana,width=50)
        txtNombre.grid(row=2, column=2)

         #Etiqueta de números atrás.
        numAtras = tk.Label(self.Ventana, 
                            text="Números del reverso", 
                            font="Verdana 12 bold",
                            bg="#000",
                            fg="#00fb33",
                            pady=20,
                            borderwidth=0)
        #Añadiendo el elemento a la ventana.
        numAtras.grid(row = 3, column = 1)
        txtAtras = tk.Entry(self.Ventana,width=50)
        txtAtras.grid(row=3,column=2) 

        #Botón para pagar
        btnPagar = tk.Button(self.Ventana,text="Pagar ahora",
                            width = 35,
                            bg = "black",
                            fg = "yellow",
                            font = "Verdana 12 bold",
                            command=self.mostrarMensaje)
        btnPagar.grid(row = 4, column = 2)

    def mostrarMensaje(self):
        MessageBox.showerror("Error", "Perdiste xD ahora me gastaré tu dinero.")