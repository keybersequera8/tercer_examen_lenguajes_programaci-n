# Grafo.py

# Se crea una estructura de grafo dirigido,
# es decir, un grafo que distingue la dirección
# de un lado, por lo que se admiten lados que
# generen un ciclo (lados de la forma nodo -> nodo):
class Grafo:
	# Se crea la lista de adyacencias del grafo dirigido: 
	def __init__(self):
		self.listaDeAdyacencias = dict()

	# Se agrega un lado al grafo:
	def agregarLado(self, nodo1, nodo2):
		# Si el nodo1 no está en el grafo y el nodo2 no está en el grafo, agrego ambos nodos y su relación:
		if (self.listaDeAdyacencias.get(nodo1, None) == None and self.listaDeAdyacencias.get(nodo2, None) == None):
			self.listaDeAdyacencias[nodo1] = []
			self.listaDeAdyacencias.get(nodo1).append(nodo2)
			self.listaDeAdyacencias[nodo2] = []
		# Si el nodo1 no está en el grafo y el nodo2 está en el grafo, agrego al nodo1 y su relación:
		elif (self.listaDeAdyacencias.get(nodo1, None) == None and self.listaDeAdyacencias.get(nodo2, None) != None):
			self.listaDeAdyacencias[nodo1] = []
			self.listaDeAdyacencias.get(nodo1).append(nodo2)
		# Si el nodo1 está en el grafo y el nodo2 no está en el grafo, agrego al nodo2 y su relación:
		elif (self.listaDeAdyacencias.get(nodo1, None) != None and self.listaDeAdyacencias.get(nodo2, None) == None):
			self.listaDeAdyacencias.get(nodo1).append(nodo2)
			self.listaDeAdyacencias[nodo2] = []
		# Si el nodo1 está en el grafo y el nodo2 está en el grafo:
		else:
			# Agrego el lado si y solo si no está en el grafo:
			if nodo2 not in self.listaDeAdyacencias.get(nodo1):
				self.listaDeAdyacencias.get(nodo1).append(nodo2)

	def __str__(self):
		cadena = ""
		for nodo in self.listaDeAdyacencias:
			cadena += f"{nodo} : ["
			nodosVecinos = self.listaDeAdyacencias.get(nodo)
			for i in range(0, len(nodosVecinos)):
				if (i != len(nodosVecinos) - 1):
					cadena += f"{nodosVecinos[i]}, "
				else:
					cadena += f"{nodosVecinos[i]}"
			cadena += "]\n"
		cadena = cadena[:-1]
		return cadena

# Clase abstracta con el método buscar para encontrar el camino de un nodo
# a otro nodo:
class Busqueda:
	def buscar(self, nodo1, nodo2):
		pass

# Clase que implementa la búsqueda en amplitud en un grafo partiendo desde
# un nodo fuente:
class BFS(Busqueda):
	def __init__(self, grafo):
		self.grafo = grafo
		self.nodoFuente = None
		self.distanciasACadaNodo = dict()
		self.nodoConsiderado = dict()

	# Se realiza la búsqueda de la distancia entre los nodos usando el 
	# algoritmo de BFS:
	def buscar(self, nodoFuente, nodoDestino):
		# Si el nodo fuente es distinto al de la última búsqueda que 
		# se realizó se debe implementar el algoritmo de BFS de lo contrario
		# no se debe volver a aplicar:
		if (self.nodoFuente != nodoFuente):
			self.nodoFuente = nodoFuente
			self.distanciasACadaNodo = dict()
			self.nodoConsiderado = dict()
			# Si el nodo fuente no está en el grafo retorno -1:
			if (nodoFuente in self.grafo.listaDeAdyacencias.keys()):
				for nodo in self.grafo.listaDeAdyacencias:
					self.distanciasACadaNodo[nodo] = -1
					self.nodoConsiderado[nodo] = False
				self.nodoConsiderado[nodoFuente] = True
				self.distanciasACadaNodo[nodoFuente] = 0
				cola = []
				cola.append(nodoFuente)
				while len(cola) != 0:
					nodoAExplorar = cola.pop(0)
					for nodo in grafo.listaDeAdyacencias.get(nodoAExplorar):
						if (self.nodoConsiderado.get(nodo) == False):
							self.nodoConsiderado[nodo] = True
							self.distanciasACadaNodo[nodo] = self.distanciasACadaNodo.get(nodoAExplorar) + 1
							cola.append(nodo)
			else:
				return -1
		return self.distanciasACadaNodo.get(nodoDestino, -1)

# Clase que implementa la búsqueda en profundidad en un grafo partiendo desde
# un nodo fuente:
class DFS(Busqueda):
	def __init__(self, grafo):
		self.grafo = grafo
		self.nodoFuente = None
		self.tiempoInicial = dict()
		self.tiempoFinal = dict()
		self.distanciasACadaNodo = dict()
		self.nodoConsiderado = dict()
		self.tiempo = 0

	# Se realiza la búsqueda de la distancia entre los nodos usando el 
	# algoritmo de DFS:
	def buscar(self, nodoFuente, nodoDestino):
		# Si el nodo fuente es distinto al de la última búsqueda que 
		# se realizó se debe implementar el algoritmo de DFS de lo contrario
		# no se debe volver a aplicar:
		if (self.nodoFuente != nodoFuente):
			self.nodoFuente = nodoFuente
			self.tiempoInicial = dict()
			self.tiempoFinal = dict()
			self.distanciasACadaNodo = dict()
			self.nodoConsiderado = dict()
			# Si el nodo fuente no está en el grafo retorno -1:
			if (nodoFuente in self.grafo.listaDeAdyacencias.keys()):
				for nodo in self.grafo.listaDeAdyacencias:
					self.nodoConsiderado[nodo] = False
				self.tiempo = 0
				self.dfsVisit(nodoFuente)
				for nodo in self.grafo.listaDeAdyacencias.keys():
					if (self.nodoConsiderado.get(nodo) == False):
						self.dfsVisit(nodo)
			else:
				return -1
		# Si el nodo final no está en el grafo se retorna -1:
		if (nodoDestino in self.grafo.listaDeAdyacencias.keys()):
			if (self.tiempoFinal.get(nodoFuente) > self.tiempoInicial.get(nodoDestino)):
				diferenciaTiemposFinales = self.tiempoFinal.get(nodoFuente) - self.tiempoFinal.get(nodoDestino)
				diferenciaTiemposIniciales = self.tiempoInicial.get(nodoDestino) - self.tiempoInicial.get(nodoFuente)
				if diferenciaTiemposFinales < diferenciaTiemposIniciales:
					return diferenciaTiemposFinales
				return diferenciaTiemposIniciales
		return -1

	# Función requerida por el algoritmo de DFS:
	def dfsVisit(self, nodo):
		self.tiempo += 1
		self.tiempoInicial[nodo] = self.tiempo
		self.nodoConsiderado[nodo] = True
		for nodoVecino in self.grafo.listaDeAdyacencias.get(nodo):
			if (self.nodoConsiderado.get(nodoVecino) == False):
				self.dfsVisit(nodoVecino)
		self.tiempo += 1
		self.tiempoFinal[nodo] = self.tiempo


print("-----------------------------------------------------")
print("Prueba del algoritmo de DFS:")
# Se crea un grafo con varios lados de la forma:
# 1 - - > 2       3
# |     ^ |     / |
# |   /   |   /   |   /- \
# v /     v v     v  v   | Un ciclo
# 4 < - - 5       6  - - /
grafo = Grafo()
grafo.agregarLado(1, 2)
grafo.agregarLado(1, 4)
grafo.agregarLado(2, 5)
grafo.agregarLado(3, 5)
grafo.agregarLado(3, 6)
grafo.agregarLado(4, 2)
grafo.agregarLado(5, 4)
grafo.agregarLado(6, 6)

print("Lista de adyacencias del grafo: ")
print(grafo)
bfs = DFS(grafo)
print(bfs.tiempoInicial)
print("Distancia del nodo 1 al 4:")
print(bfs.buscar(1, 4))  # 3
print("Distancia del nodo 1 al 5:")
print(bfs.buscar(1, 5))  # 2
print("Distancia del nodo 1 al 3:")
print(bfs.buscar(1, 3))  # -1
print("Distancia del nodo 3 al 6:")
print(bfs.buscar(3, 6))  # 1
print("-----------------------------------------------------")
print("Prueba del algoritmo de BFS:")
# Se crea un grafo con varios lados de la forma:
# 0 < - > 1       2 < - > 3
# ^       ^     ^ ^     ^ ^
# |       |   /   |   /   |
# v       v v     v v     v
# 4       5 < - > 6 < - > 7
grafo = Grafo()
grafo.agregarLado(0, 4)
grafo.agregarLado(4, 0)
grafo.agregarLado(0, 1)
grafo.agregarLado(1, 0)
grafo.agregarLado(1, 5)
grafo.agregarLado(5, 1)
grafo.agregarLado(5, 2)
grafo.agregarLado(2, 5)
grafo.agregarLado(5, 6)
grafo.agregarLado(6, 5)
grafo.agregarLado(2, 6)
grafo.agregarLado(6, 2)
grafo.agregarLado(2, 3)
grafo.agregarLado(3, 2)
grafo.agregarLado(6, 3)
grafo.agregarLado(3, 6)
grafo.agregarLado(6, 7)
grafo.agregarLado(7, 6)
grafo.agregarLado(3, 7)
grafo.agregarLado(7, 3)
print("Lista de adyacencias del grafo: ")
print(grafo)
bfs = BFS(grafo)
print("Distancia del nodo 1 al 7:")
print(bfs.buscar(1, 7))  # 3
print("Distancia del nodo 1 al 9:")
print(bfs.buscar(1, 9))  # -1
print("Distancia del nodo 5 al 7:")
print(bfs.buscar(5, 7))  # 2
print("Distancia del nodo 10 al 7:")
print(bfs.buscar(10, 7))  # -1
print("-----------------------------------------------------")
print("Fin del programa.")