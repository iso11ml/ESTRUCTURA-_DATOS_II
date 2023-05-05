'''
Alumno: Isaay Sosa Hernández 
Grupo: 5HW1
Utilice la lista enlazada para trabajar las colisiones
Actividad: Tabla Hash

'''

import math
class Node:
    def __init__(self, rfc, nombre_completo, salario):
        self.rfc = rfc
        self.nombre_completo = nombre_completo
        self.salario = salario
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, rfc, nombre_completo, salario):
        new_node = Node(rfc, nombre_completo, salario)
        new_node.next = self.head
        self.head = new_node

    def search(self, rfc):
        current = self.head
        while current:
            if current.rfc == rfc:
                return current
            current = current.next
        return None

    def delete(self, rfc):
        current = self.head
        prev = None

        while current:
            if current.rfc == rfc:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next

        return False


class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [LinkedList() for _ in range(self.size)]

    def hash_function(self, rfc):
        def custom_hash(word, value=1987):
            numberPrime1 = 31
            numberPrime2 = 51
            hash_sum = 0
            for i, char in enumerate(word):
                char_code = ord(char)
                if i % 2 == 0:
                    hash_sum += char_code * numberPrime1
                else:
                    hash_sum += char_code * numberPrime2
            aureo = (5 ** 0.5 - 1) / 2
            return int(value * ((hash_sum * aureo) % 1))
        return custom_hash(rfc) % self.size

    def insert(self, rfc, nombre_completo, salario):
        key = self.hash_function(rfc)
        trabajdor = self.table[key].search(rfc)
        if trabajdor:
            # Actualizar los datos si ya existe
            trabajdor.nombre_completo = nombre_completo
            trabajdor.salario = salario
        else:
            # Agregar nuevo trabajador
            self.table[key].insert(rfc, nombre_completo, salario)

    def search(self, rfc):
        key = self.hash_function(rfc)
        trabajdor = self.table[key].search(rfc)
        return (trabajdor.rfc, trabajdor.nombre_completo, trabajdor.salario) if trabajdor else None

    def delete(self, rfc):
        key = self.hash_function(rfc)
        return self.table[key].delete(rfc)
    
hash_table = HashTable()


bandera = -1
while bandera == -1:
    print('Bienvenido!')
    opcion = int(input('Opción:\n1.- Insertar\n2.- Buscar\n3.- Eliminar\n4.- Salir\n'))

    if opcion == 1:
        rfc = input('Ingrese el RFC: ')
        nombre_completo = input('Ingrese el nombre completo: ')
        salario = float(input('Ingrese el salario: '))
        hash_table.insert(rfc, nombre_completo, salario)
        print('Trabajador insertado con éxito.\n')
    elif opcion == 2:
        rfc = input('Ingrese el RFC: ')
        trabajdor = hash_table.search(rfc)
        if trabajdor:
            print(f"Empleado encontrado: RFC = {trabajdor[0]}, Nombre completo = {trabajdor[1]}, Salario = {trabajdor[2]}\n")
        else:
            print(f"No se encontró ningún empleado con el RFC: {rfc}\n")
    elif opcion == 3:
        rfc = input('Ingrese el RFC: ')
        result = hash_table.delete(rfc)
        if result:
            print(f"El trabajador con RFC {rfc} ha sido eliminado con éxito.\n")
        else:
            print(f"No se encontró ningún empleado con el RFC: {rfc}\n")
    elif opcion == 4:
        bandera = 1

print('Hasta luego')