#Напишите функцию, которая вычисляет наименьшее из трех чисел и выводит на экран.

#--coding:utf-8--
n = int(input())
def F(n):
  if ((n % 4 ==0) and (n % 100 !=0)) or (n % 400 ==0):
    print('високосный')
  else: 
      print('невисокосный')
print(F(n))