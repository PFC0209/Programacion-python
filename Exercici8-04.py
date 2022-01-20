print("Este programa recibe siete números y devuelve la suma.")
total=0
negatiu=0
positiu=0
Zero=0
for i in range(7):
    x = float(input("Introduce un número: "))
    if x > 0:
        positiu+=1
    elif x < 0:
        negatiu+=1
    else:
        Zero+=1
    total = total + x
print("El total es:", total)
print("Hi ha", positiu," positius, hi ha", negatiu," negatius hi ha", Zero, "zeros")
