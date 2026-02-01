#Jesús Caro Segarra

lista = []

while len(lista) < 10:
    numero = int(input("Introduce un numero: "))
    if numero <0:
        break
    lista.append(numero)
print("Lista final:", lista)