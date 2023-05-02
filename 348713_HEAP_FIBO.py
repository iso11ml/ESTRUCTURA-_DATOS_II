# '''
# Heap Fibonacci :)
# Alumno: Isaay Sosa Hernández
# Matrícula: 348713
# Elaborado: 03/03/23
# '''

# import math

# # Creación del árbol
# class FibonacciTree:
#     def __init__(self, value):
#         self.value = value
#         self.child = []
#         self.order = 0

#     # Se adiciona el nuevo árbol al conjunto de árboles
#     def add_at_end(self, t):
#         self.child.append(t)
#         self.order = self.order + 1

# # Creando el heap 
# class FibonacciHeap:
#     def __init__(self):
#         self.trees = []
#         self.least = None
#         self.count = 0

#     # Insert a node
#     def insert_node(self, value):
#         new_tree = FibonacciTree(value)
#         self.trees.append(new_tree)
#         if (self.least is None or value < self.least.value):
#             self.least = new_tree
#         self.count = self.count + 1

#     # Obtener el mínimo
#     def get_min(self):
#         if self.least is None:
#             return None
#         return self.least.value

#     # Extraer el mínimo
#     def extract_min(self):
#         smallest = self.least
#         if smallest is not None:
#             for child in smallest.child:
#                 self.trees.append(child)
#             self.trees.remove(smallest)
#             if self.trees == []:
#                 self.least = None
#             else:
#                 self.least = self.trees[0]
#                 self.consolidate()
#             self.count = self.count - 1
#             return smallest.value

#     # Consolidación de la raíz
#     def consolidate(self):
#         aux = (floor_log(self.count) + 1) * [None]

#         while self.trees != []:
#             x = self.trees[0]
#             order = x.order
#             self.trees.remove(x)
#             while aux[order] is not None:
#                 y = aux[order]
#                 if x.value > y.value:
#                     x, y = y, x
#                 x.add_at_end(y)
#                 aux[order] = None
#                 order = order + 1
#             aux[order] = x

#         self.least = None
#         for k in aux:
#             if k is not None:
#                 self.trees.append(k)
#                 if (self.least is None or k.value < self.least.value):
#                     self.least = k

#     # Muestra las raices así como el orden
#     def display_roots(self):
#         if self.trees:
#             print("Raices:")
#             for tree in self.trees:
#                 print(f"{tree.value} ({tree.order})")
#         else:
#             print("El heap Fibonacci esta vacío")

# def floor_log(x):
#     return math.frexp(x)[1] - 1

# fibonacci_heap = FibonacciHeap()

# bandera = -1;
# while(bandera == -1):
#     opcion = int(input('Opción:\n1.- Obtener el mínimo\n2.- Insertar\n3.- Eliminar el mínimo\n4.- Mostrar lista de raices\n5.- Salir\n'))
#     if opcion == 1:
#         resultado = fibonacci_heap.get_min()
#         if resultado == None:
#             print('No se han insertado valores aún\n')
#         else:
#             print(f'El mínimo es: {resultado}')
#     elif opcion == 2:
#         valor = int(input('Ingrese el valor: '))
#         fibonacci_heap.insert_node(valor)
#     elif opcion == 3:
#         resultado = fibonacci_heap.extract_min()
#         if resultado == None:
#             print('No se han insertado valores aún\n')
#         else:
#             print(f'El valor mínimo ha sido eliminado: {resultado}')
#     elif opcion == 4:
#         fibonacci_heap.display_roots()
#     elif opcion == 5:
#         bandera = 1
# print('Hasta luego')

# Este Codigo Lo Modifique Para El Proyecto
import math

# Creación del árbol
class FibonacciTree:
    def __init__(self, value, word):
        self.value = value
        self.word = word
        self.child = []
        self.order = 0

    # Se adiciona el nuevo árbol al conjunto de árboles
    def add_at_end(self, t):
        self.child.append(t)
        self.order = self.order + 1

# Creando el heap 
class FibonacciHeap:
    def __init__(self):
        self.trees = []
        self.greatest = None
        self.count = 0

    # Insert a node
    def insert_node(self, value, word):
        new_tree = FibonacciTree(value, word)
        self.trees.append(new_tree)
        if (self.greatest is None or value > self.greatest.value):
            self.greatest = new_tree
        self.count = self.count + 1

    # Obtener el máximo
    def get_max(self):
        if self.greatest is None:
            return None
        return self.greatest.word, self.greatest.value

    # Extraer el máximo
    def extract_max(self):
        largest = self.greatest
        if largest is not None:
            for child in largest.child:
                self.trees.append(child)
            self.trees.remove(largest)
            if self.trees == []:
                self.greatest = None
            else:
                self.greatest = self.trees[0]
                self.consolidate()
            self.count = self.count - 1
            return largest.word, largest.value

    # Consolidación de la raíz
    def consolidate(self):
        aux = (floor_log(self.count) + 1) * [None]

        while self.trees != []:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.value < y.value:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order = order + 1
            aux[order] = x

        self.greatest = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if (self.greatest is None or k.value > self.greatest.value):
                    self.greatest = k

    # Muestra las raices así como el orden
    def display_roots(self):
        if self.trees:
            print("Raices:")
            for tree in self.trees:
                print(f"{tree.word}: {tree.value} ({tree.order})")
        else:
            print("El heap Fibonacci está vacío")

def floor_log(x):
    return math.frexp(x)[1] - 1

fibonacci_heap = FibonacciHeap()

fibonacci_heap.insert_node(15, 'CUNA')
fibonacci_heap.insert_node(30, 'Hola')
fibonacci_heap.insert_node(10, 'GATO')
fibonacci_heap.insert_node(7, 'CASA')
# print(fibonacci_heap.get_min())
# fibonacci_heap.display_roots()
fibonacci_heap.extract_max()
# fibonacci_heap.display_roots()
# fibonacci_heap.extract_min()
# fibonacci_heap.display_roots()
print(fibonacci_heap.get_max())
fibonacci_heap.extract_max()
print(fibonacci_heap.get_max())