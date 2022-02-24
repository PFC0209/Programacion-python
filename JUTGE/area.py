import math
from operator import length_hint
from easyinput import read
x = read(int)
#resultat = []
sortida=""
b = "{area:.6f}"
for i in range(2):
    figura = read(str)
    area=0
    if figura == "rectangle":
        base = read(float)
        altura = read(float)
        area = base * altura
        b.format(area=area)
    
    if figura == "cercle":
        radi = read(float)
        area = math.pi * radi**2
        b.format(area=area)
    sortida += str(area) + '\n'
print(sortida)


