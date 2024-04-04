import random as rnd

def selec_ia():
    ia = rnd.randint(1, 3)
    options = {1: "Piedra", 2: "Papel", 3: "Tijeras"}
    result = options[ia]
    return result


opcion = 1

while opcion != 0:
    print("Selecciona tu opcion")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijeras")
    print("0. Salir")
    opcion = int(input())
    if opcion == 1:
        print("Seleccionaste piedra")
        ia = selec_ia()
        print("La ia selecciono", ia)
        if ia == "Piedra":
            print("Empate")
        elif ia == "Papel":
            print("Perdiste!")
        else:
            print("Ganaste!")
    elif opcion == 2:
        print("Seleccionaste papel")
        ia = selec_ia()
        print("La ia selecciono", ia)
        if ia == "Piedra":
            print("Ganaste!")
        elif ia == "Papel":
            print("Empate")
        else:
            print("Perdiste!")
    elif opcion == 3:
        print("Seleccionaste tijeras")
        ia = selec_ia()
        print("La ia selecciono", ia)
        if ia == "Piedra":
            print("Perdiste!")
        elif ia == "Papel":
            print("Ganaste!")
        else:
            print("Empate")
    elif opcion != 0:
        print("Inserta una opcion valida")
    else:
        print("Adios!")
