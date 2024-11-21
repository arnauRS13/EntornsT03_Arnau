'''Suma tots els elements d'una llista de dues dimensions.'''
llista = [
    [11, 9, 4, 47, 14],
    [99, 32, 30, 32, 48],
    [23, 73, 19, 56, 76],
    [8, 56, 84, 43, 95],
    [94, 52, 57, 94, 28],
    [66, 35, 39, 30, 22],
    [43, 23, 8, 15, 77],
    [91, 47, 77, 79, 3],
    [91, 0, 12, 47],
    [38, 73, 28, 17, 59]
]


suma = 0
for fila in llista:
    for element in fila:
        suma += element

print("La suma és", suma)

'''Troba el valor màxim en una llista de dues dimensions.'''
llista = [
    [11, 9, 4, 47, 14],
    [99, 32, 30, 32, 48],
    [23, 73, 19, 56, 76],
    [8, 56, 84, 43, 95],
    [94, 52, 57, 94, 28],
    [66, 35, 39, 30, 22],
    [43, 23, 8, 15, 77],
    [91, 47, 77, 79, 3],
    [91, 0, 12, 47],
    [38, 73, 28, 17, 59]
]


maxim = llista[0][0]
for fila in llista:
    for element in fila:
        if element > maxim:
            maxim = element

print("El valor màxim és", maxim)

'''Compta quantes vegades apareix un element específic en una llista de
dues dimensions.'''
llista = [
    [11, 9, 4, 47, 14],
    [99, 32, 30, 32, 48],
    [23, 73, 19, 56, 76],
    [8, 56, 84, 43, 95],
    [94, 52, 57, 94, 28],
    [66, 35, 39, 30, 22],
    [43, 23, 8, 15, 77],
    [91, 47, 77, 79, 3],
    [91, 0, 12, 47],
    [38, 73, 28, 17, 59]
]


element_especific = 5
comptador = 0
for fila in llista:
    for element in fila:
        if element == element_especific:
            comptador += 1

print(f"El {element_especific} apareix {comptador} vegades.")

'''Imprimeix els elements que es troben en posicions parells d'una llista
de dues dimensions.'''
llista = [
    [11, 9, 4, 47, 14],
    [99, 32, 30, 32, 48],
    [23, 73, 19, 56, 76],
    [8, 56, 84, 43, 95],
    [94, 52, 57, 94, 28],
    [66, 35, 39, 30, 22],
    [43, 23, 8, 15, 77],
    [91, 47, 77, 79, 3],
    [91, 0, 12, 47],
    [38, 73, 28, 17, 59]
]


for i in range(len(llista)):
    for j in range(len(llista[i])):
        if (i + j) % 2 == 0:
            print(llista[i][j], end=' ')
    print()

''' Suma els elements de la diagonal principal d'una matriu quadrada.
'''
matriu = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


suma = 0
for i in range(len(matriu)):
    suma += matriu[i][i]

print("La suma de la diagonal és", suma)

'''Transposa una matriu.
'''
matriu = [
    [11, 99, 23, 8, 94, 66, 43, 91, 38],
    [9, 92, 73, 96, 82, 85, 43, 47, 73],
    [4, 30, 19, 84, 57, 39, 87, 70, 28],
    [47, 32, 56, 43, 96, 30, 15, 7, 12, 17],
    [48, 70, 95, 22, 70, 22, 47, 59]
]


transposada = [[row[i] for row in matriu] for i in range(len(matriu[0]))]

for fila in transposada:
    print(fila)

'''Converteix tots els elements negatius d'una llista de dues dimensions a
zero.'''
matriu = [
    [1, 2, 3, -4, 5],
    [6, -7, 8, 9, -10],
    [11, 12, 13, 14, 15],
    [16, -17, 18, 19, 20],
    [-21, 22, 23, -24, -25]
]


for i in range(len(matriu)):
    for j in range(len(matriu[i])):
        if matriu[i][j] < 0:
            matriu[i][j] = 0

for fila in matriu:
    print(fila)

'''Multiplica tots els elements d'una llista de dues dimensions per una
constant K amb valor 10
'''
K = 10
llista = [
    [1, 2, 3, 0, 5],
    [6, 0, 8, 9, 0],
    [11, 12, 13, 14, 15],
    [16, 0, 19, 20],
    [21, 0, 23, 24, 0]
]


for i in range(len(llista)):
    for j in range(len(llista[i])):
        llista[i][j] *= K

for fila in llista:
    print(fila)

'''Inverteix l'ordre dels elements en cada fila d'una llista de dues
dimensions.
'''
llista = [
    [10, 20, 30, 0, 50],
    [60, 0, 80, 90, 0],
    [110, 120, 130, 140, 150],
    [160, 0, 190, 200],
    [210, 0, 230, 240, 0]
]


for i in range(len(llista)):
    llista[i] = llista[i][::-1]

for fila in llista:
    print(fila)

'''Troba l'element mínim en cada fila d'una llista de dues dimensions.'''
llista = [
    [1, 2, 3, -40, 50, 28],
    [6, 7, 8, 9, 10, 11],
    [12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22],
    [23, 24, 25, 26, 27, 28],
    [29, 30, 31, 32, 33, 34]
]


for i in range(len(llista)):
    minim = min(llista[i])
    print(f"El valor mínim de la fila {i} és {minim}.")

'''Suma els elements de cada columna en una llista de dues
dimensions.
'''
matriu = [
    [1, 2, 3, -40, 50, 28],
    [6, 7, 8, 9, 10, 11],
    [12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22],
    [23, 24, 25, 26, 27, 28],
    [29, 30, 31, 32, 33, 34]
]


suma_columnes = [0] * len(matriu[0])
for fila in matriu:
    for j in range(len(fila)):
        suma_columnes[j] += fila[j]

print("La suma de cada columna és:")
for suma in suma_columnes:
    print(suma)

'''Crea una llista amb els elements que es troben sobre la diagonal
principal d'una matriu quadrada.
'''
matriu = [
    [1, 2, 3, -40, 50, 28],
    [6, 7, 8, 9, 10, 11],
    [12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22],
    [23, 24, 25, 26, 27, 28],
    [29, 30, 31, 32, 33, 34]
]


diagonal = []
for i in range(len(matriu)):
    diagonal.append(matriu[i][i])

print("La diagonal és:")
for element in diagonal:
    print(element)

'''Comprova si totes les files d'una llista de dues dimensions tenen la
mateixa suma total.'''
matriu = [
    [1, 2, 3, -40, 50, 28],
    [6, 7, 8, 9, 10, 11],
    [12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22],
    [23, 24, 25, 26, 27, 28],
    [29, 30, 31, 32, 33, 34]
]


suma_files = [sum(fila) for fila in matriu]
mateixa_suma = all(suma == suma_files[0] for suma in suma_files)

for i, suma in enumerate(suma_files):
    print(f"La suma de la fila {i} és {suma}")

if mateixa_suma:
    print("Totes les files tenen la mateixa suma")
else:
    print("Totes les files no tenen la mateixa suma")

'''Elimina una fila específica d'una llista de dues dimensions.'''
matriu = [
    [1, 2, 3, -40, 50, 28],
    [6, 7, 8, 9, 10, 11],
    [11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22],
    [23, 24, 25, 26, 27, 28],
    [29, 30, 31, 32, 33, 34]
]


fila_a_eliminar = int(input("Quina fila vols eliminar? "))


if 0 <= fila_a_eliminar < len(matriu):
    del matriu[fila_a_eliminar]
    print("Fila eliminada correctament.")
else:
    print("Fila incorrecta.")


for fila in matriu:
    print(fila)

'''Elimina una columna específica d'una llista de dues dimensions.'''
matriu = [
    [6, 7, 8, 9, 10, 11],
    [11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22],
    [23, 24, 25, 26, 27, 28],
    [29, 30, 31, 32, 33, 34]
]

columna_a_eliminar = int(input("Quina columna vols eliminar? "))


if 0 <= columna_a_eliminar < len(matriu[0]):
    for fila in matriu:
        del fila[columna_a_eliminar]
    print("Columna eliminada correctament.")
else:
    print("Columna incorrecta.")

for fila in matriu:
    print(fila)
