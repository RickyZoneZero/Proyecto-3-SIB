#Programa que cifra los archivos a partir de una ubicación.

from cryptography.fernet import Fernet
import os

def generar_key():
    key = Fernet.generate_key()
    with open('prueba/key.key', 'wb') as key_file:
        key_file.write(key)

def cargar_key():
    return open('prueba/key.key', 'rb').read()

def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)

def cifrar():

    path_to_encrypt = r'C:\Users\enriq\Desktop\Proyecto_3_SIB\secrets'
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]

    generar_key()
    key = cargar_key()

    encrypt(full_path, key)