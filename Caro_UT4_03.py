#Jesús Caro Segara

notas = []

for i in range(5):
    nota = float(input("Introduce un nota (0-10): "))
    notas.append(nota)

print("Notas:", notas)
print("Media:", sum(notas) / len(notas))
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))


