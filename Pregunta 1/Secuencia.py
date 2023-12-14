# Secuencia.py

# Ejecución:
# 	python3 Secuencia.py

# Estudiante: Keyber Yosnar Sequera Avendaño.
# Carnet: 16-11120.

# Se crea una clase Secuencia cuyos métodos son 
# heredados por las clases Pila y Cola.

class Secuencia:
	# Agrega un elemento en la secuencia:
	def agregar(self, elemento):
		pass
	# Remueve un elemento de la secuencia:
	def remover(self, elemento):
		pass
	# Retorna true si la secuencia está vacía,
	# false en caso contrario:
	def vacio(self):
		pass

class Pila(Secuencia):
	# Se crea el constructor de la clase:
	def __init__(self):
		self.pila = []
	# Se agrega un elemento en la pila:
	def agregar(self, elemento):
		self.pila.append(elemento)
	# Se elimina el último elemento en la pila:
	def remover(self):
		if (self.vacio() == False):
			self.pila.pop()
	# Retorna true si la pila está vacía, en caso
	# contrario retorna false:
	def vacio(self):
		if (len(self.pila) == 0):
			return True
		return False
	# Representación de la pila como string:
	def __str__(self):
		cadena = "["
		for i in range(0, len(self.pila)):
			if (i != len(self.pila)-1):
				cadena += f"{self.pila[i]}, "
			else:
				cadena += f"{self.pila[i]}"
		cadena += "]"
		return cadena

class Cola(Secuencia):
	# Se crea el constructor de la clase:
	def __init__(self):
		self.cola = []
	# Se agrega un elemento en la cola :
	def agregar(self, elemento):
		self.cola.append(elemento)
	# Se elimina el primer elemento en la cola:
	def remover(self):
		if (self.vacio() == False):
			self.cola.pop(0)
	# Retorna true si la cola está vacía, en caso
	# contrario retorna false:
	def vacio(self):
		if (len(self.cola) == 0):
			return True
		return False
	# Representación de la cola como string:
	def __str__(self):
		cadena = "["
		for i in range(0, len(self.cola)):
			if (i != len(self.cola)-1):
				cadena += f"{self.cola[i]}, "
			else:
				cadena += f"{self.cola[i]}"
		cadena += "]"
		return cadena

# Prueba de la clase pila:
print("-------------------------------------------------")
print("Prueba de la clase Pila:")
print("Se crea una pila vacía:")
pila = Pila()       
print(pila)         # [] Pila vacía
print("Se agregan tres elementos a la pila:")
pila.agregar(1)
pila.agregar(2)
pila.agregar(3)
print(pila)         # [1, 2, 3]
print("Se remueve un elemento de la pila:")
pila.remover()
print(pila)         # [1, 2]
print("Se comprueba si la pila está vacía:")
print(pila.vacio()) # False

# Prueba de la clase cola:
print("-------------------------------------------------")
print("Prueba de la clase Cola:")
print("Se crea una cola vacía:")
cola = Cola()       
print(cola)         # [] cola vacía
print("Se agregan tres elementos a la cola:")
cola.agregar(1)
cola.agregar(2)
cola.agregar(3)
print(cola)         # [1, 2, 3]
print("Se remueve un elemento de la cola:")
cola.remover()
print(cola)         # [2, 3]
print("Se comprueba si la cola está vacía:")
print(cola.vacio()) # False
print("-------------------------------------------------")
print("Fin del programa.")