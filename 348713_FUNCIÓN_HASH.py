'''
Isaay Sosa Hernández
Grupo: 5HW1
Fecha de elaboración: 26-04-23
"Estructura De Datos II
'''
import math
import matplotlib.pyplot as plt
value = 1987

# def HashFunction(word):
#     newWord = [ord(caracter) for caracter in word]
#     orderWord = sorted(newWord, reverse = True)
#     for character in range (0, len(orderWord)):
#         if character <= round(len(newWord)):
#             suma += orderWord[character]
#         else:
#             multiplicacion += 100 * orderWord[character]
#         # value = (value * 31 + (ord(letra) - ord('a') + 1)) % 1987
    

value = 1987
# def HashFunction(word):
#     newWord = [ord(caracter) for caracter in word]
#     #orderWord = sorted(newWord, reverse=True)
#     suma = 0
#     multiplicacion = 0
#     for character in range(0, len(newWord)):
#         if character <= round(len(newWord)/2):
#             suma += newWord[character]2
#             multiplicacion += 100 * newWord[character]
#     total = suma + multiplicacion
#     aureo =  (5 ** 0.5 - 1) / 2
#     return int(value * ((total * aureo) % 1))
    # return (suma + multiplicacion) % value

def HashFunction(word, value = 1987):
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
    pi = math.pi
    # print(hash_sum * aureo)
    # print((hash_sum * aureo) % 1)
    return int(value * ((hash_sum * aureo) % 1))

def ReadWords():
    dictionary = {}
    with open('348713_BANCO_PALABRAS.txt', 'r') as f:
        for line in f:
            word = line.strip()
            key = HashFunction(word)
            if key in dictionary: 
                dictionary[key] += 1
            else: 
                dictionary[key] = 0
    return dictionary

bandera = -1
resultado = ReadWords()
while(bandera == -1):
    opcion = int(input('Opción:\n1.- Mostrar Diccionario\n2.- Mostrar Histograma\n3.- Salir\n'))
    if opcion == 1:
        print(resultado)
    elif opcion == 2:
        keys = list(resultado.keys())
        values = list(resultado.values())
        plt.bar(keys, values)
        plt.title("Gráfica De Colisiones")
        plt.ylabel("No.Colisiones")
        plt.xlabel("Posición Del Arreglo");
        # plt.show()
        # data_groups = [values[i:i+497] for i in range(0, len(values), 497)]
        # fig, axs = plt.subplots(2, 2, figsize=(20, 10))
        # for i in range(4):
        #     row = i // 2
        #     col = i % 2
        #     axs[row][col].bar(range(len(data_groups[i])), data_groups[i])
        #     axs[row][col].set_title(f'Grupo {i+1}')
        #     axs[row][col].set_xlabel('Posición del arreglo')
        #     axs[row][col].set_ylabel('No. colisiones')
        plt.show()
# Create the figure and axis objects
    elif opcion == 3:
        bandera = 1
print('Hasta luego!')


# "La música de los números primos" de Marcus du Sautoy: