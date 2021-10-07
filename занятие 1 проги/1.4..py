# Переменная seconds хранит в себе некоторое количество секунд. Переведите это число в дни:часы:минуты:секунды.
# -- coding: utf-8--
seconds = int(input('Введите количество секунд:'))

dnei = seconds // 86400
chasov = (seconds % 86400) // 3600
minut = ((seconds % 86400) % 3600) // 60
sec = ((seconds % 86400) % 3600) % 60
print(dnei, 'суток', chasov, 'часов', minut, 'минут', sec, 'секунд')