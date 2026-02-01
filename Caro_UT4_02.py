lista1=[]
for i in range(5):
    ciudad = input("Introduce un ciudad: ")
    lista1.append(ciudad)

listacopia=[]
for i in range(4,-1,-1):
    listacopia.append(lista1[i])
    print("Lista ordenada", lista1)
    print("Lista al reves",listacopia)




