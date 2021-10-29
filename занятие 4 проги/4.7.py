#Dана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.
# -- coding: utf-8 --
stroka = input('введите строку')
def F(stroka):
    stroka = stroka[:stroka.find('h')] +stroka[stroka.rfind('h') + 1:]
    print(stroka)
F(stroka)