#Jesus Caro Segarra

#Pedir al usuario cuántas pizzas quiere
pizzas = int(input("¿Cuantas pizzas quieres? "))

#Precios fijos

precio_pizza = 5
precio_envio_pizza = 2
tarifa_plana = 9

#Cálculos

precio_opccion_1 = (precio_pizza * precio_envio_pizza) * pizzas
precio_opccion_2 = precio_pizza * pizzas + tarifa_plana

#Resultados

print(f"Opcción 1 - Pizza/s + envio/S : {precio_opccion_1} €")
print(f"Opcción 2 - Tarifa plana : {precio_opccion_2} €")

#Opció más económica
if precio_opccion_1 < precio_opccion_2:
    print("La opción más económica es: Opción 1 - Pizza/s + envio/S ")
elif precio_opccion_2 < precio_opccion_1:
    print("La opción más económica es: Opción 2 - Tarifa plana ")
else:
    print("Las dos opciones tienen el mismo precio")
