a, b, c = int(input()), int(input()), int(input())
ma = (a, b, c)
mi = (a, b, c)
if ma == a and mi == b:
    print(a)
    print(b)
    print(c)
elif ma == b and mi == c:
    print(b)
    print(a)
    print(c)
elif ma == c and mi == a:
    print(c)
    print(b)
    print(a)



#a, b, c, d, f = int(input()), int(input()), int(input()), int(input()), int(input())
#print('Наименьшее число = ', min(a,b,c,d,f))
#print('Наибольшее число = ', max(a,b,c,d,f))

#num = float(input())
#print(round(num - int(num), 2))
