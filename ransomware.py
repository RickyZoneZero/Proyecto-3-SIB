import rescueWindow
import pathlib
#Programa que contiene la función principal para ejecutar el proyecto.

def main():
    rescueWindow.rescueWindow() 

main()

ejemplo_dir = 'C:/' #Muestra una lista de archivos que contiene la unidad C
directorio = pathlib.Path(ejemplo_dir)
for fichero in directorio.iterdir():
    print(fichero.name)
