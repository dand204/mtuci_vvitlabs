import math
k = list()
exp1 = exp2 = 0
print("Введите коэффиценты квадратного уравнения последовательно через ENTER")
for i in range(3):
    k.append(int(input()))
print("Решаемое уравнение: ", (str(k[0]) + "x^2") , "+", (str(k[1]) + "x") , "+", k[2])
d = (k[1]**2) - (4 * k[0] * k[2])
print("Дискрименант: %.2f" % d)
if d > 0:
    exp1 = (-(k[1]) + math.sqrt(d)) / 2*k[0]
    exp2 = (-(k[1]) - math.sqrt(d)) / 2*k[0]
    print("Корнями являются:", ("%.2f" % exp1) , "и", ("%.2f" % exp2))
elif d == 0:
    exp1 = (-(k[1]) + math.sqrt(d)) / 2*k[0]
    print("Корнями являются:", ("%.2f" % exp1))
else:
    print("Корни невозможно извлечь, т.к дискрименант меньше нуля")
    



