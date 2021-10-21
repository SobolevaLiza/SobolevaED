#По данному натуральному n вычислите сумму 1^3+2^3+3^3+...+n^3
n = int(input('введите натуральное число: '))
sum = 0
for i in range (n):
    sum = sum + i**3
   # print(i**3, sum)
print(sum)
    