'''Fes un programa en Python que comprovi que s’ha introduït una lletra per teclat (només d’una) 
i després que comprovi si la lletra introduïda és una vocal o bé una consonant. 
Operador in i funció len. '''

# Demanar que l'usuari introdueixi una lletra
lletra = input("Introdueix una lletra: ").lower()

# Comprovem que s'ha introduït només una lletra
if len(lletra) == 1 and lletra.isalpha():  # Comprovem que és una lletra i que només té un caràcter
    # Verifiquem si la lletra és una vocal
    if lletra in 'aeiou':
        print(f"La lletra '{lletra}' és una vocal.")
    else:
        print(f"La lletra '{lletra}' és una consonant.")
else:
    print("Si us plau, introdueix només una lletra.")
