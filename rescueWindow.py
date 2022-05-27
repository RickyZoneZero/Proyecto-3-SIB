import images
#Librería para los elementos de la GUI.
import tkinter as tk  	

class rescueWindow(object):
    Ventana = tk.Tk()

    def __init__(self):	#Constructor.
        self.crearVentana()	#Llamada al método crearVentana.
    
    def crearVentana(self):	#Método para crear la ventana.
        self.Ventana.title("R4Ns0mW4r3 d3cr1pt0R 2.0")	#Título de la ventana.
        #self.Ventana.overrideredirect(1) #Esconde la barra superior.
        self.Ventana.attributes('-toolwindow', True) #No permite modificar atributos de la ventana.
        self.Ventana.geometry("1000x750+300+50")	#Tamaño de la ventana.
        self.Ventana.configure(bg = "Red")		#Color de fondo.

        #Etiqueta de encabezado.
        encabezado = tk.Label(self.Ventana, text="Ooops, your files have been encrypted! xD", font="Verdana 18 bold")
        #Configuración de color de fondo y de la fuente de etiqueta.
        encabezado.config(bg="Red",fg="white")
        #Añadiendo el elemento a la ventana.
        encabezado.grid(row = 0, column = 1) 

        #Imagen de candado
        imgCandado = tk.PhotoImage(file="images\candado.png")
        etqCandado = tk.Label(image = imgCandado)
        #Añadiendo el elemento a la ventana.
        etqCandado.grid(row = 0, column = 0)
        
        self.Ventana.mainloop()		#Muestra la ventana.