'''
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания.
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона),
сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие
минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)
и целевую функцию для нахождения оптимального  решения.
Вариант 18. Имеется некоторая сумма денег. Сформируйте разные варианты ее размещения в К банках.
Использование минимальной суммы в банке и шага распределения
При нечётном шаге распределения в нечетных банках храниться нечетное количество валюты
'''
import itertools

summ = int(input("Сколько денег будет размещенно : "))
step = int(input("Шаг для распределения валюты : "))
min = int(input("Минимальная сумма размещения в банке : "))
k = int(input("Количество банков : "))
odd = step % 2 != 0
ans = input("Какой функцией выводить ответ? 1 : Алгоритмический 2 : Itertools\n- ")
c = int(input("Количество выводимых вариантов : "))

bk = []
for i in range(k):
    bk.append("Банк №{}".format(i+1))

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

bks = []
d = 0
def shuflebk(order, bk):
    global bks
    global d
    if d <= 0:
        d = c
        return
    if len(order) == k:
        if not(order in bks) and ((not odd) or all(list(map(lambda x: x % 2 != 0, order[::2])))):
            bks.append(order)
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

a = []
a.append([])
for i in range(k):
    a[0].append(min)
    summ -= min
    if summ < 0:
        a[0][-1] += summ
        summ = 0

da = c//2
shufle(summ, a[0])
a.pop(0)

if ans == '1':
    print("Результат работы собственное функции")
    for i in a:
        bks = []
        d = c
        shuflebk([], i)
        for j in bks:
            for l in range(k):
                print(bk[l], ' : ', j[l], end=' | ')
            print()
            c -= 1
            if c == 0: break
        if c == 0: break

elif ans == '2':
    print('Результат работы функции itertools')
    for i in a:
        bks = list(itertools.permutations(i, k))
        nbks = []
        nbks.extend(bks)
        for j in nbks:
            bks.remove(j)
            if not(j in bks) and ((not odd) or all(list(map(lambda x: x % 2 != 0, j[::2])))):
                bks.append(j)
        for j in bks:
            for l in range(k):
                print(bk[l], ' : ', j[l], end=' | ')
            print()
            c -= 1
            if c == 0: break
        if c == 0: break
