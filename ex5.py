'''Escriu un programa que implementi el següent diagrama de flux. Les dades s’introdueixen per teclat:'''



# Benvinguda al jugador
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("Left or right? ").lower()
if direction == "left":  # Si va a l'esquerra
    swim = input("Swim or wait? ").lower()
    if swim == "wait":  # Si espera
        door = input("Which door? ").lower()
        if door == "yellow":  # Porta groga
            print("You win!")
        elif door == "red":  # Porta vermella
            print("Burned by fire. Game over!")
        elif door == "blue":  # Porta blava
            print("Eaten by beasts. Game over!")
        else: 
            print("Game over!")
    else:  
        print("Attacked by trout. Game over!")
else:  # Si va a la dreta
    print("Fall into a hole. Game over!")