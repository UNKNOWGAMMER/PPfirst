import math
a = int (input('введите a '))
b = int (input('введите b '))
c = int (input('введите c '))
D = b*b-4*a*c
print ('дискриминант= ' ,D)
if D<0:
    print("корней нет")
else:
    print("корни есть")
    Koren = math.sqrt(D)

    x3 =(-b + Koren)/(2*a)
    x4 = (-b - Koren)/(2*a)

    print("Первая вариация ",x3,)
    print("Вторая вариация ",x4,)