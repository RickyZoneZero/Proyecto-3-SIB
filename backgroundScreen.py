import images
#Biblioteca de funciones externas para poder cambiar el fondo de pantalla
# utilizando dll's de Windows.
import ctypes


#Parámetro de interfaz
SPI_SETDESKWALLPAPER = 20 
#Interfaz directa de Windows para cambiar la imagen de fondo.
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "images/ransomware.png" , 0)