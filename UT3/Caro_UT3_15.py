#Jesús Caro Segarra

num1 = int(input("Primero numero: "))
num2 = int(input("Segundo numero: "))

inicio = min(num1, num2)
fim = max(num1, num2)

for i in range(inicio, fim+1):
    if i % 2 == 0:
        print(i)