'''
Вариант 18. Имеется некоторая сумма денег. Сформируйте разные варианты ее размещения в К банках.
Использование минимальной суммы в банке и шага распределения
При нечётном шаге распределения в нечетных банках храниться нечетное количество валюты
'''
import itertools
import math
from tkinter import *
from tkinter import ttk

summ = 1 #int(input("Сколько денег будет размещенно : "))
step = 1 #int(input("Шаг для распределения валюты : "))
min_ = 1 #int(input("Минимальная сумма размещения в банке : "))
k = 1 #int(input("Количество банков : "))
odd = True #step % 2 != 0
c = 1 #int(input("Количество выводимых вариантов : "))
itstrs = []
funcstrs = []

root = Tk()
root.geometry('900x900')
root.resizable(False, False)

labelc = ttk.Label(text="Количество выводимых вариантов: ")
labelc.place(anchor=NW, x = 30, y = 100, height = 25)
entryc = ttk.Entry()
entryc.place(anchor=NW, x = 250, y = 100, height = 25, width = 80)

labelsmm = ttk.Label(text="Сумма денег на распределение: ")
labelsmm.place(anchor=NW, x = 30, y = 20, height = 25)
entrysmm = ttk.Entry()
entrysmm.place(anchor=NW, x = 250, y = 20, height = 25, width = 80)

labelstep = ttk.Label(text="Шаг распределения: ")
labelstep.place(anchor=NW, x = 380, y = 20, height = 25)
entrystep = ttk.Entry()
entrystep.place(anchor=NW, x = 600, y = 20, height = 25, width = 80)

labelmin_ = ttk.Label(text="Минимальная сумма в банке: ")
labelmin_.place(anchor=NW, x = 30, y = 60, height = 25)
entrymin_ = ttk.Entry()
entrymin_.place(anchor=NW, x = 250, y = 60, height = 25, width = 80)

labelk = ttk.Label(text="Количество банков: ")
labelk.place(anchor=NW, x = 380, y = 60, height = 25)
entryk = ttk.Entry()
entryk.place(anchor=NW, x = 600, y = 60, height = 25, width = 80)

labelit = ttk.Label(text="Результат Itertools : ")
labelit.place(anchor=NW, x = 30, y = 140, height = 25, width = 240)

labelal = ttk.Label(text="Результат алгоритма : ")
labelal.place(anchor=NW, x = 30, y = 500, height = 25, width = 240)

def drawScroll():
    itlist = StringVar(value=itstrs)
    listboxd = Listbox(listvariable=itlist)
    listboxd.place(anchor=NW, x=30, y=170, width=840, height=320)

    scrollbar = ttk.Scrollbar(orient="vertical", command=listboxd.yview)
    scrollbar.place(anchor=NW, y=170, x=850, width=20, height=320)
    listboxd["yscrollcommand"] = scrollbar.set

    funclist = StringVar(value=funcstrs)
    listboxt = Listbox(listvariable=funclist)
    listboxt.place(anchor=NW, x=30, y=530, width=840, height=320)

    scrollbar = ttk.Scrollbar(orient="vertical", command=listboxt.yview)
    scrollbar.place(anchor=NW, y=530, x=850, width=20, height=320)
    listboxt["yscrollcommand"] = scrollbar.set


drawScroll()

#функция без встроенных функций питона
da = 0
def shufle(sum_, b):
    global a
    global da
    if da <= 0:
        return
    if sum_ == 0:
        a.append(b)
        da -= 1
        return
    nb = []
    nb.extend(b)  # Питон добавляет массив, изменения в котором изменяют больший
    for i in range(k):
        if sum_ == 0: break
        nb[i] += step
        sum_ -= step
        if sum_ < 0:
            nb[i] += sum_
            sum_ = 0
        shufle(sum_, nb)


bksf = []
bksit = []
a = []
d = 0
def shuflebk(order, bk):
    global bksf
    global d
    if d <= 0:
        d = c
        return
    if len(order) == k:
        if not(order in bksf) and ((not odd) or all(list(map(lambda x: x % 2 != 0, order[::2])))):
            bksf.append(order)
            d -= 1
        return
    for i in bk:
        nbk = []
        nbk.extend(bk)
        nbk.remove(i)
        norder = []
        norder.extend(order)
        norder.append(i)
        shuflebk(norder, nbk)


def main():
    global c
    global summ
    global step
    global min_
    global k
    global odd
    global bksf
    global bksit
    global bk
    global itstrs
    global funcstrs
    global da
    global d
    global a

    try:
        summ = int(entrysmm.get())
        step = int(entrystep.get())
        min_ = int(entrymin_.get())
        k = int(entryk.get())
        c = int(entryc.get())
        c1 = int(entryc.get())
        odd = step % 2 != 0
    except:
        return

    bk = []
    for i in range(k):
        bk.append("Банк №{}".format(i + 1))

    a = []
    a.append([])
    for i in range(k):
        a[0].append(min_)
        summ -= min_
        if summ < 0:
            a[0][-1] += summ
            summ = 0

    da = c//2
    shufle(summ, a[0])
    a.pop(0)

    funcstrs = []
    for i in a:
        bksf = []
        d = c
        shuflebk([], i)
        for j in bksf:
            funcstrs.append('')
            for l in range(k):
                funcstrs[-1] += bk[l] + ' : ' + str(j[l]) + ' | '
            funcstrs[-1] += '\n'
            c -= 1
            if c == 0: break
        if c == 0: break

    itstrs = []
    for i in a:
        bksit = list(itertools.permutations(i, k))
        nbks = []
        nbks.extend(bksit)
        for j in nbks:
            bksit.remove(j)
            if not(j in bksit) and ((not odd) or all(list(map(lambda x: x % 2 != 0, j[::2])))):
                bksit.append(j)
        for j in bksit:
            itstrs.append('')
            for l in range(k):
                itstrs[-1] += bk[l] + ' : ' + str(j[l]) + ' | '
            itstrs[-1] += '\n'
            c1 -= 1
            if c1 == 0: break
        if c1 == 0: break

    drawScroll()


btn = ttk.Button(text="Рассчитать", command=main)
btn.place(anchor=NW, x = 380, y = 100, height = 25, width = 100)

root.mainloop()