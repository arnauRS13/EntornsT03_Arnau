'''Implementa un control d’accés a una atracció.  
Genera totes les dades aleatòriament: l’alçada (entre 100cm i 210cm, 
l’edat (entre 10 i 25 anys) i si vol fotos (cert o fals). 
Ha de seguir el diagrama de flux. 
Has d'informar si pot pujar a l’atracció o no, i en cas que si en funció de l’edat 
i si volen fotos o no has cobrar un preu o un altre.
'''


import random

# Generem les dades aleatòriament
alçada = random.randint(100, 210)  # Alçada entre 100 cm i 210 cm
edat = random.randint(10, 25)      # Edat entre 10 i 25 anys
vol_fotos = random.choice([True, False])  # Si volen fotos (cert o fals)

# Mostrem les dades generades
if vol_fotos:
    vol_fotos_str = 'Sí'
else:
    vol_fotos_str = 'No'

print(f"Alçada: {alçada} cm")
print(f"Edat: {edat} anys")
print(f"Vol fotos: {vol_fotos_str}")

# Comprovem si pot pujar a l'atracció
if alçada >= 120 and edat >= 12:
    print("Pot pujar a l'atracció.")

    # Calculem el preu
    if edat < 18:
        preu = 5  # Preu per menors de 18 anys
    else:
        preu = 10  # Preu per adults

    if vol_fotos:
        preu += 3  # Cost addicional per les fotos

    print(f"El preu a pagar és de {preu} €.")

else:
    print("No pot pujar a l'atracció.")
