# По данному натуральном n вычислите сумму 1!+2!+3!+...+n!.
# В решении этой задачи можно использовать только один цикл
# -- coding: utf-8 --
n = int(input('Введите чило: '))
factorial = 1
summa = 0
for i in range (1, n + 1):
    factorial = factorial * i
    summa = summa + factorial
print(summa)