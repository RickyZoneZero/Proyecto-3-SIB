#Programa que descifra los archivos a partir de una ubicación.

from cryptography.fernet import Fernet
import os

def cargar_key():
    return open('prueba/key.key', 'rb').read()

def decrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(item, 'wb') as file:
            file.write(decrypted_data)

def descifrar():
    path_to_encrypt = r'C:\Users\enriq\Desktop\Proyecto_3_SIB\secrets'
    #os.remove(path_to_encrypt+'\\'+'readme.txt')

    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]

    key = cargar_key()
    decrypt(full_path, key)