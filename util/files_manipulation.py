import os
import shutil

def files_names_read_from_dir(files_to_read_path):
    """Devuelve los nombres de los archivos que se encuenetran en un directorio dado

    Argumentos:
    files_to_read_path -- Ruta del directorio que contiene los archivos que se quieren leer
    """
    files_names = []
    files = os.listdir(files_to_read_path)
    for f in files:
        if f != '.gitignore':
            files_names.append(f)
    return files_names

def move_files(origin_path, destination_path):
    """ Mueve todos los archivos existentes en un directorio de origen a uno de destino

    Argumentos:
    origin_path -- ruta relativa al directorio que contiene los archivos que se quierer mover
    destination_path -- ruta relativa al directorio a donde serán movidos los archivos
    """
    current_path = os.getcwd() + os.sep

    files_to_move = files_names_read_from_dir(origin_path)

    for file in files_to_move:
        origin = current_path + origin_path + file
        destination = current_path + destination_path + file

        if os.path.exists(origin):
            shutil.move(origin, destination)
            print('El archivo ha sido movido a', origin)
        else:
            print('No existe archivo para mover')

# move_files('COAs'+os.sep, '.coas_por_enviar'+os.sep) # Línea para probar la ejecuión correcta de este script