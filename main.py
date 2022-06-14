#Наибольшие числа. На вход программе подается натуральное число n, а затем nnn различных натуральных чисел, каждое на отдельной строке.(n≥2). Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.







#Знакочередующаяся сумма. На вход программе подается натуральное число n. Напишите программу вычисления знакочередующей суммы 1−2+3−4+5−6+…+(-1)^{n+1}n.
n = int(input())
s = 0 
for i in range(1, n + 1, 1):
    if i % 2 == 0:
        s -= i
    else:
        s += i
print(s)





#Сумма делителей. На вход программе подается натуральное число nnn. Напишите программу, которая вычисляет сумму всех его делителей.
#n = int(input())
#s = 0
#for i in range(1, n + 1):
#    if n % i == 0:
#        s += i
#print(s)
        






#Без нулей. Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел. Гарантируется, что хотя бы одно из 10 чисел является ненулевым.
#p = 1
#for i in range(10):
#    num = int(input())
#    if num != 0:
#        p *= num
#print(p)


#Факториал На вход программе подается натуральное число n. Напишите программу, которая вычисляет n!.Факториалом натурального числа nnn, называется произведение всех натуральных чисел от 1 до n, то есть n!=1*2*3*…*n.
#n = int(input())
#f = 1
#for i in range(1, n + 1):
#    f *= i
#print(f)




#Сумма чисел 2 На вход программе подается натуральное число n. Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно) квадрат которых оканчивается на 2, 5 или 8. Если таких чисел нет в указанном диапазоне, то следует вывести 0.
#n = int(input())
#s = 0
#for i in range(1, n + 1):
#    if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
#        s += i
#print(s)





#Асимптотическое приближение
#На вход программе подается натуральное число n. Напишите программу, которая вычисляет значение выражения (1+1/2 +1/3+…+1/n)−ln(n).
#Для вычисления натурального логарифма воспользуйтесь функцией log(n), которая находится в модуле math.
#from math import log
#n = int(input())
#num = 0
#for i in range(1, n + 1):
#    num += 1 / i 
#print(num - log(n))




#Сумма чисел
#На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке. Напишите программу, которая подсчитывает сумму введенных чисел.
#n = int(input())
#s = 0
#for i in range(n):
#    num = int(input())        
#    s += num
#print(s)




#Количество чисел
#На вход программе подаются два целых числа a и b (a≤b). Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b включительно, куб которых оканчивается на 4 или 9.
#count = 0
#a, b = int(input()), int(input())
#for i in range(a, b + 1):
#    if i**3 % 10 == 4 or i**3 % 10 == 9:
#        count += 1
#print(count)




#Таблица умножения
#Дано натуральное число n. Напишите программу, которая выводит таблицу умножения на n.
#n = int(input())
#for i in range(1, 11):
#    print(f'{n} x {i} =', i * n)





#Последовательность чисел 4
#Даны два натуральных числа m и n ( m ≤ n). Напишите программу, которая выводит все числа от m до n включительно удовлетворяющие хотя бы одному из условий:
#    число кратно 17;
#    число оканчивается на 9;
#    число кратно 3 и 5 одновременно.
#m, n = int(input()), int(input())
#for i in range(m, n +1):
#    if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
#        print(i)





# Последовательность чисел 3 
# Даны два целых числа m и n (m > n). Напишите программу, которая выводит все нечетные числа от m до n включительно в порядке убывания.
#m, n = int(input()), int(input())
#for i in range(m, n - 1, -1):
#    if i % 2 != 0:
#        print(i)




# Последовательность чисел 2
# Даны два целых числа m и n. Напишите программу, которая выводит все числа от m до n включительно в порядке возрастания, если m < n, или в порядке убывания в противном случае.
#m, n = int(input()), int(input())
#if m < n:
#     for i in range(m, n + 1):
#        print(i)
#else:
#    for i in range(m, n - 1, -1):
#        print(i)


# Последовательность чисел 1
#m, n = int(input()), int(input())
#for i in range(m, n + 1):
#    print(i)




# На вход программе подается три натуральных числа m, p, n:
#    m: стартовое количество организмов;
#    p: среднесуточное увеличение в %;
#    n: количество дней для размножения.
# Напишите программу, которая предсказывает размер популяции организмов. Программа должна выводить размер популяции в каждый день, начиная с 1 и заканчивая nnn-м днем.
#m, p, n = int(input()), int(input()), int(input())
#for i in range(n):
#    print(i + 1, m)
#    m += m * p / 100




# Звездный треугольник
#n = int(input())
#for i in range(n, 0, -1):
#    print('*' * i)


# Квадрат числа
#n = int(input())
#for i in range(n + 1):
#    print(f'Квадрат числа {i} равен {i**2}')




# Повторяй за мной
#st = input()
#for i in range(10):
#    print(i, st)



# Звездный прямоугольник
#n = int(input())
#for i in range(n):
#    print('*' * 19)

#for i in range(6):
#    print('A' * 3)
#for i in range(5):
#    print('B' * 4)
#print('E')
#for i in range(9):
#    print('T' * 5)
#print('G')



# Площадь правильного многоугольника с длиной стороны a и количеством сторон n
#from math import *
#n, a = int(input()), float(input())
#S = n * pow(a, 2) / (4 * tan(pi / n))
#print(S)


#Даны три вещественных числа  a, b, c. Напишите программу, которая находит вещественные корни квадратного уравнения 
#from math import *
#a, b, c = float(input()), float(input()), float(input())
#D = pow(b, 2) - (4 * a * c)
#print(D)
#if D > 0:
#    x1 = (-b - sqrt(D)) / (2 * a)
#    x2 = (-b + sqrt(D)) / (2 * a)
#    print(min(x1, x2))
#    print(max(x1, x2))
#elif D == 0:
#    print(-b / (2 * a))
#elif D < 0:
#    print('Нет корней')


#Пол и потолок
#from math import *
#x = float(input())
#print(ceil(x) + floor(x))


#Напишите программу, вычисляющую значение тригонометрического выражения
#from math import *
#x = float(input())
#x = radians(x)
#print(sin(x) + cos(x) + pow(tan(x), 2))


# Средние значения
#from math import sqrt
#a, b = float(input()), float(input())
#print((a + b) / 2)  # среднее арифметическое чисел a и b
#print(sqrt(a * b))  # среднее геометрическое чисел a и b 
#print(2 * a * b / (a + b))  # среднее гармоническое чисел a и b
#print(sqrt((a**2 + b**2) / 2))  # среднее квадратичное чисел a и b 


# Кратчайшее расстояние
#from math import *
#x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
#p = sqrt(pow(x1 -x2, 2) + pow(y1 - y2, 2))
#print(p)






#Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. Напишите программу проверяющую корректность email адреса.
#st = input()
#if '@' in st and '.' in st:
#    print('YES')
#else:
#    print('NO')



#Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае
#st = input()
#if 'суббота' in st or 'воскресенье' in st:
#    print('YES')
#else:
#    print('NO')



# Вводится строка. Программа считывает одну строку, после чего выводит «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.
#st = input()
#if 'синий' in st:
#    print('YES')
#else:
#    print('NO')





# Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.
#st1, st2, st3 = input(), input(), input()
#maxx = max(len(st1), len(st2), len(st3))
#minn = min(len(st1), len(st2), len(st3))
#mid = (len(st1) + len(st2) + len(st3)) - (maxx + minn)
#if  abs(mid - minn) == abs(maxx - mid):
#    print('\033[2;31;43mYES\033[0m')
#else:
#    print('\033[2;31;43mNO\033[0m')

# Многократный запуск программы
#flag = True
#while flag:
#    num_1, num_2 = int(input('Введите первое число ')),int(input('Введите второе число '))
#    s = num_1 + num_2
#    print(f'Сумма чисел равна {s}')
#    f = input('Для продолжения введите "Y" и нажмте ENTER, для завершения "N"\n')
#    if f == 'n':
#        flag = False

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
#print(min(a, b, c, key=len ))
#print(max(a, b, c, key=len ))
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
