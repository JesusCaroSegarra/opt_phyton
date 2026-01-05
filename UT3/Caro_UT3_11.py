#Jesús Caro Segarra

import random

numero_secreto = random.randint(1, 100)
intentos = 10
while intentos > 0:
    num = int(input("Introduce un numero entre 1 y 100: : "))
    intentos -= 1

    if num == numero_secreto:
        print(f"¡Correcto! Lo has acertado en ¨{10 - intentos} intentos.")
        break
    elif num < numero_secreto:
        print("El numero secreto es mayor")
    else:
        print("El numero secreto es menor")

        print("Intentos restantes: ", intentos)

    if intentos == 0 and num != numero_secreto:
        print("Has perdido. El numero secreto era: ", numero_secreto)