# -- coding: utf-8--
N = int(input('введите целое число, не меньшее 2: '))
i = 2
while N % i != 0:
    i +=1 
print(i)