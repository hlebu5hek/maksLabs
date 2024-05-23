'''
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания.
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона),
сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие
минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)
и целевую функцию для нахождения оптимального  решения.
Вариант 18. Имеется некоторая сумма денег. Сформируйте разные варианты ее размещения в К банках.
'''
import itertools

summ = int(input("Сколько денег будет размещенно : "))
k = int(input("Количество банков : "))

ans = input("Какой функцией выводить ответ? 1 : Алгоритмический 2 : Itertools\n- ")
c = int(input("Количество выводимых вариантов : "))

bk = []
for i in range(k):
    bk.append("Банк №{}".format(i+1))

#функция без встроенных функций питона
def shufle(sum_, b):
    global a
    if sum_ == 0:
        a.append(b)
        return
    nb = []
    nb.extend(b)  # Питон добавляет массив, изменения в котором изменяют больший
    for i in range(k):
        if sum_ == 0: break
        nb[i] += 1
        sum_ -= 1
        if sum_ < 0:
            nb[i] += sum_
            sum_ = 0
        shufle(sum_, nb)

bks = []
def shuflebk(order, bk):
    global bks
    if len(order) == k:
        if not(order in bks): bks.append(order)
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
a.append([1] * k)
summ -= k

shufle(summ, a[0])
a.pop(0)

if ans == '1':
    print("Результат работы собственное функции")
    for i in a:
        bks = []
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
            if not(j in bks):
                bks.append(j)
        for j in bks:
            for l in range(k):
                print(bk[l], ' : ', j[l], end=' | ')
            print()
            c -= 1
            if c == 0: break
        if c == 0: break
