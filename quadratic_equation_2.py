from time import sleep
import colorama
from colorama import Back, Style, Fore
import re
import matplotlib.pyplot as plt
colorama.init()
koefs = None
while koefs != '':
     print (Fore.MAGENTA +'''Эта программа работает с квадратными уравнениями и функциями.
Находит корни квадратных уравнений, 
Их вершины. точки,
А так же строит график квадратичной функции''',Style.RESET_ALL)
     sleep(0.3)
     print(Fore.RED +'Введите коэфиценты a,b,c через пробел соответсвенно. \nЕсли хотите выйти, нажмите "Enter" \
без ввода данных. ',Style.RESET_ALL)
     print(Fore.RED +"Коэфиценты: ",Style.RESET_ALL, end = '')
     koefs = str(input())
     try:
        koef = re.split(' ',koefs)
        if len(koef) == 3:
            a = float(koef[0])
            b = float(koef[1])
            c = float(koef[2])
        elif len(koef) == 2:
            a = float(koef[0])
            b = float(koef[1])
            c = 0
        elif len(koef) > 3:
            print ("Вы ввели коэфицентов дофига.\nВведите коэффиценты ещё раз\
Их должно быть 3 или 2(в случае если с=0)")
            continue
        elif len(koef) == 1:
            print("\nА чё так мало то :|\nЕще раз введите 3 числа или 2(в случае если с=0)\n")
            continue
     except ValueError:
         print("\nВы ввели ввели коэфиценты неправильно. Я не могу их распознать:(\nПопробуйте еще раз\n")
         continue
     D = b**2 - 4*a*c
     if D > 0 :
          X1 = (-b + D ** (0.5))/(2*a)
          X2 = (-b - D ** (0.5))/(2*a)
          print (Fore.RED +'Корни квадратного уровнения:',Style.RESET_ALL)
          sleep(0.3)
          print(Back.BLUE +'X1 =',X1,Style.RESET_ALL)
          sleep(0.3)
          print(Back.BLUE +'X2 =',X2,Style.RESET_ALL)
          sleep(0.3)
     elif D == 0:
             X = -b/2*a
             print (Fore.RED +'корень квадратного уровнения:',Style.RESET_ALL)
             sleep(0.3)
             print(Back.BLUE +' X=',X,Style.RESET_ALL)
             sleep(0.3)
     else:
         print(Back.BLUE +'Нет корней',Style.RESET_ALL)
         sleep(0.3)

     if D>=0:
         verchx0 = -b/(2*a)
         verchy0 = a * (verchx0)**2 + (b * verchx0) + c
         print(Fore.RED +'Координаты вершины квадратного уравнения: ',Style.RESET_ALL)
         print(Back.GREEN +'(',str(verchx0),';', str(verchy0),')',Style.RESET_ALL,sep = '')
         sleep(0.3)
         print(Fore.RED +'Направление ветвей параболы: ',Style.RESET_ALL)
         if a > 0:
              print(Back.GREEN +'Ветви направлены Вверх, тк а > 0',Style.RESET_ALL)
              sleep(0.3)
         elif a < 0:
              print(Back.GREEN +' Ветви направлены вниз, тк а < 0',Style.RESET_ALL)
              sleep(0.3)
         else :
             print(Back.GREEN +'Получится прямая:/',Style.RESET_ALL)
             sleep(0.3)

         i = -3.0
         p = 1.0
         print(Fore.RED +'Точки для графика:',Style.RESET_ALL)
         ygrafic = []
         xgrafic = []
         while i < 0:
             y = a * (verchx0 + i)**2 + (b * (verchx0 + i)) + c
             print(Back.RED + str(p),'-ая точка: (',str(verchx0) + str(i),';',str(y),')',Style.RESET_ALL, sep = '')
             xgrafic.append(verchx0 + i)
             ygrafic.append(y)
             i = i+1.0
             p = p+1.0
             sleep(0.3)
         if i==0:
            print(Back.RED + str(p),'-ая точка: (',str(verchx0),';', str(verchy0),')',Style.RESET_ALL, sep = '')
            xgrafic.append(verchx0)
            ygrafic.append(verchy0)
            i=i+1.0
            p=p+1.0
            sleep(0.3)
         while i <= 3:
             y = a * (verchx0 + i) ** 2 + (b * (verchx0 + i)) + c
             print(Back.RED +str(p), '-ая точка: (', str(verchx0) + str(i), ';', str(y), ')',Style.RESET_ALL, sep = '')
             xgrafic.append(verchx0 + i)
             ygrafic.append(y)
             i = i + 1.0
             p = p + 1.0
             sleep(0.3)
         plt.plot(xgrafic,ygrafic)
         plt.show()




    
    
    
