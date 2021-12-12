#Напишите функцию, которая вычисляет наименьшее из трех чисел и выводит на экран.

#--coding:utf-8--
one=int(input('введите первое число: '))
two=int(input('введите второе число: '))
three=int(input('введите третье число: '))
def F(one,two,three):
  if (one < three) and (one < two):
    return one
  elif two < three: return two
  else: return three
print(F(one,two,three))