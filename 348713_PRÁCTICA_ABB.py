#Nombre: Isaay Sosa Hernández Grupo 5HW3 Fecha de elaboración: 31 De Enero de 2023
import numpy as np

MAX = 100
VACIO = -999

nodo_anterior = -1
arbol = np.full(100, VACIO)

def Left(n):
    return 2 * n + 1

def Right(n):
    return 2 * n + 2

def Root(n):
    return(n - 1) / 2

def Search(x, posicion):
    global nodo_anterior
    posicion_correspondiente = -1
    if posicion < MAX:
        if arbol[posicion] != VACIO:
            if arbol[posicion] == x:
                posicion_correspondiente = posicion
            elif x < arbol[posicion]:
                nodo_anterior = posicion
                posicion_correspondiente = Search(x, Left(posicion))
            else: 
                nodo_anterior = posicion
                posicion_correspondiente = Search(x, Right(posicion))
    return posicion_correspondiente

def Insertion(x):
    posicion_correspondiente = -1 
    posicion_actual = Search(x, 0)
    if posicion_actual < 0:
        if(arbol[0] == VACIO):
            posicion_correspondiente = 0
        elif x < arbol[nodo_anterior]:
            posicion_correspondiente = Left(nodo_anterior)
        else:
            posicion_correspondiente = Right(nodo_anterior)

        if posicion_correspondiente < MAX:
            arbol[posicion_correspondiente] = x
        else:
            posicion_correspondiente = -1  
            
    return posicion_correspondiente  
        
def Max(posicion):
    while arbol[posicion] != VACIO:
        nodo_anterior = posicion
        posicion = Right(posicion)
        if arbol[posicion] == VACIO:
            posicion = nodo_anterior
            break  

    return posicion

def Min(posicion):
    while arbol[posicion] != VACIO:
        nodo_anterior = posicion
        posicion = Left(posicion)
        if arbol[posicion] == VACIO:
            posicion = nodo_anterior
            break  
        
    return posicion

def Eliminate(x):
    bandera = False
    posicion_actual = Search(x, 0)

    if posicion_actual >= 0:
        left_value = Left(posicion_actual)
        right_value = Right(posicion_actual)
        if arbol[left_value] == VACIO and arbol[right_value] == VACIO:
            arbol[posicion_actual] = VACIO
            bandera = True
        elif arbol[left_value] == VACIO or arbol[right_value] == VACIO:
            if left_value == VACIO:
                nieto = right_value
            else:
                nieto = left_value
            arbol[posicion_actual] = nieto
            arbol[nieto] = VACIO
            bandera = True
        else:
            if arbol[posicion_actual] < arbol[0]:
                padre = Max(Left(0))
            else:
                padre = Min(Right(0))
            arbol[posicion_actual] = arbol[padre]
            arbol[padre] = VACIO
            bandera = True

    return bandera

def Show():
    for i in range(0, arbol.size):
        if arbol[i] != VACIO:
            print(f'{i}: {arbol[i]}')
    
def Archivo():
        with open('348713_ARCHIVO_ARBOL.txt', mode = 'r') as FILE:
            arreglo = np.genfromtxt(FILE, dtype = 'int' , delimiter = "\n")
            for i in range(0, arreglo.size):
                Insertion(arreglo[i])
bandera = -1
Archivo()

while(bandera == -1):
    opcion = int(input('Opción:\n1.- Buscar\n2.- Insertar\n3.- Eliminar\n4.- Valor máximo\n5.- Valor minímo\n6.- Mostrar árbol\n7.- Salir\n'))
    if opcion == 1:
        valor = int(input("Ingrese el valor que desea buscar: "))
        resultado = Search(valor, 0)
        if resultado < 0:
            print('El valor no existe :(')
        else:
            print(f' El valor se encuentra en la posición {resultado}')
    elif opcion == 2:
        valor = int(input('Ingrese el valor va a insertar: '))
        resultado = Insertion(valor)
        if resultado < 0: 
            print(f'El valor {valor} no se intertó!')
        else: 
            print(f'El valor {valor} se insertó en la posición {resultado} ')
    elif opcion == 3:
        valor = int(input('Ingrese el valor que desea eliminar: '))
        bandera2 = Eliminate(valor)
        if bandera2 == False:
            print('El valor no se eliminó debido a que no existe!!')
        else:
            print('Eliminación exitosa!!')
    elif opcion == 4:
        valor = Max(0)
        if arbol[valor] == VACIO:
            print('No hay datos en el árbol')
        else:
            print(f'El máximo es: {arbol[valor]}')
    elif opcion == 5:
        valor = Min(0)
        if arbol[valor] == VACIO:
            print('No hay datos en el árbol')
        else:
            print(f'El mínimo es: {arbol[valor]}')
    elif opcion == 6:
        Show()
    elif opcion == 7:
        bandera = 1
print('Hasta luego')

