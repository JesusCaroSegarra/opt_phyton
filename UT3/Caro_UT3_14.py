#Jesús Caro Segarra

while True:
    caracter = input("Introduce un caracter (espacio para terminar): ")
    if caracter == " ":

        break

    if caracter.lower() in "aeiou":
        print("VOCAL")
    else:
        print("NO VOCAL")