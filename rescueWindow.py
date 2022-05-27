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
        self.Ventana.geometry("1000x568+500+250")	#Tamaño de la ventana.

        #Configuración de renglones y columnas.
        self.Ventana.columnconfigure(1, weight=1)
        self.Ventana.columnconfigure(3, pad=7)
        self.Ventana.rowconfigure(3, weight=1)
        self.Ventana.rowconfigure(5, pad=7)

        #Imagen de fondo
        img = tk.PhotoImage(file="images/fondo.png")
        label = tk.Label(self.Ventana,image=img)
        label.place(x=0, y=0)


        #Imagen de craneo
        imgCran = tk.PhotoImage(file="images/craneo.png")
        labelCran = tk.Label(self.Ventana,
                            image=imgCran,
                            bg="#fff",
                            borderwidth=0)
        labelCran.grid(row = 2, column = 1)

        #Etiqueta de encabezado.
        encabezado = tk.Label(self.Ventana, 
                            text="Ooops, tus archivos importantes han sido cifrados! xD", 
                            font="Verdana 18 bold",
                            bg="#fff",
                            fg="#00fb33",
                            pady=20,
                            borderwidth=0)
        #Añadiendo el elemento a la ventana.
        encabezado.grid(row = 0, column = 2) 

        #Etiqueta de tiempo.
        tiempo = tk.Label(self.Ventana, text="Tiempo restante", 
                            font="Verdana 18 bold",
                            bg="#fff",
                            fg="#00fb33",
                            borderwidth=0)
        #Añadiendo el elemento a la ventana.
        tiempo.grid(row = 3, column = 1)
        
        self.Ventana.wm_attributes("-transparentcolor", 'white') #Línea para dar transparencia.
        self.Ventana.mainloop()		#Muestra la ventana.