import pathlib

ejemplo_dir = 'C:/' #Muestra una lista de archivos que contiene la unidad C
directorio = pathlib.Path(ejemplo_dir)
for fichero in directorio.iterdir():
    print(fichero.name)
