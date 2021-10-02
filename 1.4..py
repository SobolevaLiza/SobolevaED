# Переменная seconds хранит в себе некоторое количество секунд. Переведите это число в дни:часы:минуты:секунды.
seconds = int(input('Введите количество секунд:'))
if seconds > 60:
    print((seconds // 60), 'минут')
if seconds > 3600:
    print((seconds // 3600), 'часов')
if seconds > 86400:
    print((seconds // 86400), 'дней')
