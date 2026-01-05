#Jesús Caro Segarra

cantidad = int(input("Cuantos numeros vas a introducir?: "))

mayores = 0
menores = 0
ceros = 0

for i in range(cantidad):
    num = int(input("Introduce un numero: "))
    if num > 0:
        mayores += 1
    elif num < 0:
        menores += 1
    else:
        ceros += 1

print("Mayores que cero: ", mayores)
print("Menores que cero: ", menores)
print("Iguales  que cero: ", ceros)