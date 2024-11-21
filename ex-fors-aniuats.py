'''1. Quadrat de caràcters: Imprimeix un quadrat de n x n asteriscs (*).'''
c = "*"
n = 5
for i in range (n):
    for j in range(n):
        print(c, end = "  ")
    print()
    
'''2. Triangle rectangle: Imprimeix un triangle rectangle de n files d'asteriscs.
'''
c = "*"
n = 5
for i in range (1, n, +1):
    for j in range(i):
        print(c, end = " ")
    print()
    
'''3. Triangle rectangle invertit: Imprimeix un triangle rectangle invertit de n files d'asteriscs.'''

c = "*"
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print(c, end=" ")
    print()


'''4. Piràmide: Imprimeix una piràmide de n files d'asteriscs.'''

n = 5  
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

'''
Piràmide: Imprimeix una piràmide de n files d'asteriscs.
'''
n = 5  

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)


'''
Piràmide invertida: Imprimeix una piràmide invertida de n files d'asteriscs.
'''
n = 5  

for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)


'''
Quadrat buit: Imprimeix un quadrat buit de n x n amb les vores d'asteriscs.
'''
n = 5  

for i in range(n):
    if i == 0 or i == n - 1:
        print('* ' * n)
    else:
        print('* ' + '  ' * (n - 2) + '*')


'''
Quadrat amb diagonal: Imprimeix un quadrat de n x n amb una diagonal d'asteriscs.
'''
n = 5 

for i in range(n):
    for j in range(n):
        if i == j:
            print('*', end=' ')
        else:
            print('#', end=' ')
    print()


'''
X de caràcters: Imprimeix una X en una quadrícula de n x n d'asteriscs.
'''
n = 5 

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()


'''
Quadrat amb creu: Imprimeix un quadrat de n x n amb una creu al centre.
'''
n = 5 

for i in range(n):
    for j in range(n):
        if i == n // 2 or j == n // 2:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()


'''
Nombres seqüencials: Imprimeix un quadrat de n x n amb nombres seqüencials de 0 a 14.
'''
n = 15 

for i in range(n):
    for j in range(n):
        print(j, end=" ")
    print()


'''
Caràcters alternants: Imprimeix un quadrat de n x n alternant entre '-' i '#'.
'''
n = 5  

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()


'''
Triangle de caràcters alternants: Imprimeix un triangle amb n files alternant entre '-' i '#'.
'''
n = 5  

for i in range(n):
    for j in range(i + 1):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()
