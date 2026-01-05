#Jesús Caro Segarra

suma = 0
contador = 0

while True:
    num = int(input("Ingresa un numero: "))
    if num == 0:
        break
    suma += num
    contador += 1

    if contador > 0:
        media = suma / contador
        print("Suma:", suma)
        print("Media:", media)

    else:
        print("No se han introducido números ")