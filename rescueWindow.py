#Programa que muestra la ventana de rescate.

#Paquete de otra carpeta.
import images

#Librería para los elementos de la GUI.
import tkinter as tk  	
import time
import datetime

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

        #Reloj
        #Timer
        hours = 0 #Inicializando temporizador.
        minutes = 0
        seconds = 20

        #Definiendo los segundos de las cifras de horas y minutos
        s_horas = hours * 3600
        s_minutos = minutes * 60

        # Cálculo de número total de segundos
        total_seconds = s_horas + s_minutos + seconds
    
        #Mientras segundos sea menor que cero, va a decrementar en uno.
        while total_seconds > 0:
    
            temp = datetime.timedelta(seconds = total_seconds)
            string = temp
            reloj = tk.Label(self.Ventana, text = string,
                            font="Verdana 18 bold",
                            bg="#fff",
                            fg="#00fb33",
                            borderwidth=0)
        #Añadiendo el elemento a la ventana.
            reloj.grid(row = 4, column = 1)
            time.sleep(1)
            total_seconds -= 1
    
        print("Bzzzt! El tiempo terminó! Perdiste...")
        
        #Mensaje
        mensaje = """Tus archivos importantes han sido cifrados. Entre ellos se encuentran documentos, fotos y videos comprometadores que te podrían generar problemas. 
que hacer?
Tienes el tiempo marcado en la ventana para poder pagar $5000 dólares en bitcoin. 
Puedes pagar dando click en el botón inferior, que te redigirá a los datos de pago.

Date prisa! :v, porque el tiempo corre y el juego acaba de comenzar."""

        #Área de texto
        area = tk.Text(self.Ventana, height=13, width=65)
        area.tag_configure('color',
                    foreground='#00fb33',
                    font=('Verdana', 12, 'bold'))
        area.insert(tk.END, mensaje, 'color')
        area.grid(row = 3, column = 2)

        #Botón para pagar
        btnPagar = tk.Button(self.Ventana,text="Pagar",
                            width = 25,
                            bg = "black",
                            fg = "yellow",
                            font = "Verdana 12 bold")
        btnPagar.grid(row = 4, column = 2)
        
        self.Ventana.wm_attributes("-transparentcolor", 'white') #Línea para dar transparencia.
        self.Ventana.mainloop()		#Muestra la ventana.