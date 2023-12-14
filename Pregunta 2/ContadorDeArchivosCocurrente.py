# ContadorDeArchivosConcurrente.py

# Ejecución:
#       python3 ContadorDeArchivosConcurrente.py

# Estudiante: Keyber Yosnar Sequera Avendaño.
# Carnet: 16-11120

# Se crea una función que cuenta los archivos dentro
# del subarbol de un directorio.

import os
import concurrent.futures

# Función para contar archivos en un directorio:
def contadorArchivos(directorio):
    contador = 0
    for nombreDeArchivo in os.listdir(directorio):
        if os.path.isfile(os.path.join(directorio, nombreDeArchivo)):
            contador += 1
    return contador

# Función para contar archivos en un subárbol de directorios de forma concurrente:
def contadorArchivosEnElSubarbol(directorioRaiz):
    with concurrent.futures.ThreadPoolExecutor() as contador:
        # Crear una lista para almacenar las cuentas obtenidas:
        cuentas = []
        # Recorrer el subárbol de directorios:
        for direccion, nombresDeDireccion, filenames in os.walk(directorioRaiz):
            # Crear un hilo por cada subdirectorio
            for nommbreDeDireccion in nombresDeDireccion:
                directorio = os.path.join(direccion, nommbreDeDireccion)
                cuentas.append(contador.submit(contadorArchivos, directorio))
        # Sumar los resultados para obtener el total de archivos
        archivosTotales = sum(cuenta.result() for cuenta in cuentas)
        # Se cuentan los archivos del directorio raiz:
        archivosTotales += contadorArchivos(directorioRaiz)
    return archivosTotales

# ---------------------------------------------------------------------------------------------------
# Probar la función
directorioRaiz = "/home/keyber8888/programas/python" # Modificarlo al directorio de su preferencia...
# El directorio es de la forma:
# carpeta1
# | archivo1
# | archivo2
# | archivo3
# | archivo4
# carpeta2
# | archivo1
# | archivo2
# | archivo3
# | archivo4
# archivo1
# archivo2
archivosTotales = contadorArchivosEnElSubarbol(directorioRaiz)
print("-------------------------------------------------------------")
print(f"El total de archivos en el subárbol es: {archivosTotales}") # 8 para el caso propuesto:
print("-------------------------------------------------------------")
print("Fin del programa.")