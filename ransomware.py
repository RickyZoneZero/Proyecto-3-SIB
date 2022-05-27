#Programa que contiene la función principal para ejecutar el proyecto.

#Paquetes de otras carpetas.
import rescueWindow, backgroundScreen

#Librería para manejar tiempo.
import time

#Función principal
def main():
    backgroundScreen
    time.sleep(5)
    rescueWindow.rescueWindow() 

#Llamada a función principal
main()
