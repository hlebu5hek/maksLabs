"""
Задана рекуррентная функция. Область определения функции – натуральные числа.
 Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
  Определить границы применимости рекурсивного и итерационного подхода.
   Результаты сравнительного исследования времени вычисления представить в табличной и графической форме в виде отчета по лабораторной работе.
18.	F(1) = 2; G(1) = 1; F(n) =(-1)n*( F(n–1) – G(n–1) /(2n)!), G(n) = F(n–1) + G(n–1), при n >=2"""

import math
import time
import matplotlib.pyplot as plt
from functools import lru_cache

n=-1

timer=[]
timer_rec=[]

def factrial(x):
    s = 1
    for i in range(2, x+1):
        s*=i
    return s

#рекурсия

lru_cache(maxsize=None)
def rec_f(x):
    if x < 2:
        return 1
    else:
        return (-1)**int(n*(rec_f(x-1) - rec_g(x-1)/factrial(2*n)))

lru_cache(maxsize=None)
def rec_g(x):
    if x < 2:
        return 1
    else:
        return rec_f(x-1)+rec_g(x-1)

#итерация
def it_f(x):
    f=[1]*3
    g=[1]*3
    for i in range(2,x+1):
        g[1] = f[0]+g[0] #либо cata_f[0]
        f[-1] = (-1)**int(n*(f[0] - g[0]/factrial(2*n))) #либо Х
        f[0], f[1] = f[1], f[2]
        g[0], g[1] = g[1], g[2]

    return f[-1], g[-1]

while n < 1:
    print("Введите натуральное число от 1 ")
    n = int(input())


graf = list(range(1, n+1))

for i in graf:
    start = time.time()
    result = it_f(i)[0]
    end = time.time()
    timer.append(end-start)
    start_rec = time.time()
    res = rec_f(i)
    end_rec = time.time()
    timer_rec.append(end_rec-start_rec)
    rec_times = end_rec-start_rec
    iter_times = end-start
    print("\n", i, "результат рекурсии ",
          res,"---------результат итерации",
          result,"-----------время  РЕКУРСИИ ",
          end_rec-start_rec,"-------время  ИТЕРАЦИИ",end-start, sep='\n')

plt.plot(graf, timer, label='Итерационная функция.')
plt.plot(graf, timer_rec, label='Рекусионная функция.')
plt.legend(loc=2)

plt.xlabel('Значение n')
plt.ylabel('Время выполнения (c)')
plt.show()