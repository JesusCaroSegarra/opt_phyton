#Jesús Caro Segarra

lista1 = []
lista2 = []

for i in range(5):
    lista1.append(int(input("Introduce un número para la lista 1: ")))

for i in range(5):
    lista2.append(int(input("Introduce un número para la lista 2: ")))

lista_resultado = lista1 + lista2

print("Listas combinadas:", lista_resultado)