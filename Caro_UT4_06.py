#Jesús Caro Segarra

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Novimbre", "Dicembre"]

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mes = 0
while mes < 1 or mes > 12:
    if mes > 12:
        print("Introduce un número entre 1 y 12")
    mes = int(input("Ingrese un numero de mes (1-12): "))

print("El mes es:", meses[mes - 1])
print("Los días son:", dias[mes - 1])
