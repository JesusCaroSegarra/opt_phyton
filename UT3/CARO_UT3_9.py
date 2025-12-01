#Jesús Caro Segarra

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
c = float(input("Introduce el tercer número: "))

numeros = [a, b, c]
numeros.sort(reverse=True)

print("Ordenados de mayor a menor:", numeros)
