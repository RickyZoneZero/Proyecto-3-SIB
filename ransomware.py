#Programa que contiene la función principal para ejecutar el proyecto.

#Paquetes de otras carpetas.
import rescueWindow, backgroundScreen, cipher

#Librería para manejar tiempo.
import time

#Función principal
def main():
    cipher.cifrar()
    backgroundScreen
    time.sleep(5)
    rescueWindow.rescueWindow() 
    
#Llamada a función principal
main()
