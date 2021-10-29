#Пользователь вводит строку и символ для удаления. Необходимо удалить этот символ из всей строки.
# -- coding: utf-8 --
str = input('введите строку:  ')
symbol = input('введите символ:  ')
def F(str, symbol):
    print(str.replace(symbol, ''))
F(str, symbol)
