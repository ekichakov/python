#Площадь правильного многоугольника с длиной стороны aaa и количеством сторон n
from math import *
n, a = int(input()), float(input())
S = n * pow(a, 2) / (4 * tan(pi / n))
print(S)



# Возрастающая арифметическая прогрессия из строки
#st1, st2, st3 = input(), input(), input()
#ma = max(st1, st2, st3, key=len)
#mi = min(st1, st2, st3, key=len)
#mid = (int(len(st1)) + int(len(st2)) + int(len(st3))) - (int(ma) + int(mi))
#if mi<mid<ma:
#    print('YES')
#else:
#    print('NO')



# Определение самого короткого и самого длинного названия города
#a, b, c = str(input()), str(input()), str(input())
print(min(a, b, c, key=len ))
print(max(a, b, c, key=len ))
# Определение самого короткого и самого длинного названия города
#city_1, city_2, city_3 = input(), input(), input()
#ma = max(len(city_1), len(city_2), len(city_3))
#mi = min(len(city_1), len(city_2), len(city_3))
#if ma == len(city_1) and mi == len(city_2):
#    print(city_2)
#    print(city_1)
#elif ma == len(city_1) and mi == len(city_3):
#    print(city_3)
#    print(city_1)
#elif ma == len(city_2) and mi == len(city_3):
#    print(city_3)
#    print(city_2)
#elif ma == len(city_2) and mi == len(city_1):
#    print(city_1)
#    print(city_2)
#elif ma == len(city_3) and mi == len(city_1):
#    print(city_1)
#    print(city_3)
#elif ma == len(city_3) and mi == len(city_2):
#    print(city_2)
#    print(city_3)






#football_team = input()
#print(f'Футбольная команда {football_team} имеет длину {len(football_team)} символов')





#lst = [1, 2, 3, 4]
#print(lst)
# сортировка трёх чисел от большего к меньшему
#a, b, c = int(input()), int(input()), int(input())
#ma = max(a, b, c)
#mi = min(a, b, c)
#print(ma)
#print((a + b + c) - (ma + mi))
#print(mi)

#a, b, c, d, f = int(input()), int(input()), int(input()), int(input()), int(input())
#print('Наименьшее число = ', min(a,b,c,d,f))
#print('Наибольшее число = ', max(a,b,c,d,f))

#num = float(input())
#print(round(num - int(num), 2))
