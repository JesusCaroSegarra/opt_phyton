#Jesús Caro Segarra

import random
lista_numeros =[]
for i in range (10):
    lista_numeros.append(random.randint(1,10))
    for num in lista_numeros:
        print(num,"al cuadrado es", num ** 2 )
