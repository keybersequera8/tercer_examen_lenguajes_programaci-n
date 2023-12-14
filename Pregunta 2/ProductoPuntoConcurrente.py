# ProductoPunto.py

# Ejecución:
#       python3 ProductoPuntoConcurrente.py

# Estudiante: Keyber Yosnar Sequera Avendaño.
# Carnet: 16-11120.

# Se crea una función que calcula el producto punto de dos vectores
# de manera concurrente, si las dimensiones de los vectores pasados 
# a la función no son las mismas se retorna None.

import concurrent.futures

# Función para calcular el producto de dos elementos:
def multiplicar(x, y):
    return x * y

# Función para calcular el producto punto de forma concurrente:
def productoPuntoConcurrente(vector1, vector2):
    if (len(vector1) == len(vector2)):
        with concurrent.futures.ThreadPoolExecutor() as multiplicador:
            # Calcular el producto de los elementos correspondientes en los vectores
            resultados = multiplicador.map(multiplicar, vector1, vector2)
            # Sumar los resultados para obtener el producto punto
            productoPunto = sum(resultados)
    else:
        productoPunto = None
    return productoPunto

# Prueba de algunos productos puntos entre vectores:

# Calcular el producto punto
productoPunto = productoPuntoConcurrente([1,2,3], [4,5,6])    
print("---------------------------------------------------------------")
print(f"El producto punto de los vectores [1,2,3] y [4,5,6] es: {productoPunto}")     # 32
productoPunto = productoPuntoConcurrente([1,2,3], [4,5,6,7])
print("---------------------------------------------------------------")
print(f"El producto punto de los vectores [1,2,3] y [4,5,6,7] es: {productoPunto}")   # None pues las dimensiones de los vectores son distintas
productoPunto = productoPuntoConcurrente([], [])
print("---------------------------------------------------------------")
print(f"El producto punto de los vectores [] y [] es: {productoPunto}")               # 0
print("---------------------------------------------------------------")
print("Fin del programa.")