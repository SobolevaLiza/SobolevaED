#Напишите функцию, которая вычисляет наименьшее из трех чисел и выводит на экран.

#--coding:utf-8--
def F():
  a = int(input())
  aa = int(input())
  b = int(input())
  bb = int(input())
  if((1 <= a <= 8) and (1 <= aa <= 8) and (1 <= b <= 8) and (1 <= bb <= 8)):
        if(((a % 2 != 0) and (aa % 2 != 0)) or ((a % 2 == 0) and (aa % 2 == 0))):
            kto = "Чёрный"
        else:
            fkto = "Белый"
        if(((b % 2 != 0) and (bb % 2 != 0)) or ((b % 2 == 0) and (bb % 2 == 0))):
            chto = "Чёрный"
        else:
            chto = "Белый"
        if(chto == kto):
            return "Да"
        else:
            return "Нет"
print(F())