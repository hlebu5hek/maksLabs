'''Вариант 18
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N),
состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется
случайным образом целыми числами в интервале [-10,10].
Для тестирования использовать не случайное заполнение, а целенаправленное.
d e
c b
Для простоты все индексы в подматрицах относительные.
По сформированной матрице F (или ее частям) необходимо вывести не менее 3 разных графиков.
Программа должна использовать функции библиотек numpy  и mathplotlib #print(int(np.linalg.det(np.array(a))))
Формируется матрица F следующим образом: скопировать в нее А и
если в С количество чисел, больших К в нечетных столбцах, чем произведение чисел в нечетных строках,
то поменять местами С и В симметрично, иначе С и Е поменять местами несимметрично.
При этом матрица А не меняется. После чего если определитель матрицы А
больше суммы диагональных элементов матрицы F, то вычисляется выражение: A*AT – K * F-1,
иначе вычисляется выражение (A-1 +G-FТ)*K,
где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно.
'''
from random import randint as rnd
import numpy as np
import matplotlib.pyplot as plt

def printList(z):
    for i in z:
        for j in i:
            print("{:7}".format(round(j, 2)), end=' ')
        print()
    print()

k, n = int(input("k = ")), int(input("n = "))
m = n//2
n = m*2
a = []

for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(rnd(-10,10))

print("Матрица A : ")
printList(a)

b = []
c = []
d = []
e = []
for i in range(m):
    b.append([])
    c.append([])
    d.append([])
    e.append([])
    for j in range(m):
        b[i].append(a[i+m][j+m])
        c[i].append(a[i+m][j])
        d[i].append(a[i][j])
        e[i].append(a[i][j+m])

print("Матрица B : ")
printList(b)
print("Матрица C : ")
printList(c)
print("Матрица D : ")
printList(d)
print("Матрица E : ")
printList(e)

count_ = 0
for i in range(m):
    for j in range(1, m, 2):
        if(c[i][j] > k): count_ += 1
print("В С количество чисел, больших К в нечетных столбцах = ", count_)

mult_ = 1
for i in range(1, m, 2):
    for j in range(m):
        mult_ *= c[i][j]
print("В С произведение чисел в нечетных строках = ", mult_)

if count_ > mult_:
    print("Количество чисел, больших К, больше произведения\n")
    for i in range(m):
        for j in range(m):
            c[i][j], b[i][j] = b[i][m-j-1], c[i][m-j-1]
else:
    print("Количество чисел, больших К, меньше произведения\n")
    for i in range(m):
        for j in range(m):
            c[i][j], e[i][j] = e[i][j], c[i][j]

f = []
f.extend(d)
f.extend(c)
for i in range(m):
    f[i].extend(e[i])
for i in range(m, n):
    f[i].extend(b[i-m])

print("Матрица F : ")
printList(f)

a_ar = np.array(a)
deta = np.linalg.det(a_ar)
a_ar_tr = a_ar.transpose()

sum_ = 0
for i in range(n):
    sum_ += f[i][i]

if deta > sum_: #A * AT – K * F-1
    print("Определитель A ({:1}) больше суммы диагональных элементов F ({:2})\n".format(int(deta), sum_))
    a_arr_mul_trans = np.matmul(a_ar, a_ar_tr)
    print("A * AT : ")
    printList(list(a_arr_mul_trans))

    f_arr_inv = np.linalg.inv(np.array(f))
    f_arr_inv *= k
    print("K * F-1 : ")
    printList(list(f_arr_inv))

    out_ = np.add(a_arr_mul_trans, (-1)*f_arr_inv)
    print("A * AT – K * F-1 : ")
    printList(list(out_))

else: #(A-1 + G - FТ) * K
    print("Определитель A ({:1}) меньше суммы диагональных элементов F ({:2})\n".format(int(deta), sum_))
    print("A-1 : ")
    a_inv = np.linalg.inv(a_ar)
    printList(list(a_inv))

    f_arr_tr = np.array(f)
    f_arr_tr = f_arr_tr.transpose()
    print("FT : ")
    printList(list(f_arr_tr))

    g = np.tril(a_ar, 0)
    print("G : ")
    printList(list(g))

    out_ = np.add(a_inv, g)
    out_ = np.add(out_, (-1)*f_arr_tr)
    out_ *= k
    print("(A-1 + G - FТ) * K : ")
    printList(list(out_))

plt.title("Зависимости: y = sin от элементов F, x = соs от элементов F")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(np.cos(f),np.sin(f),linestyle="--",color="r")

plt.show()

plt.title("Высота столбца от числа элемента первой строки")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.bar(range(0,n),f[0],color='r',alpha=0.9)

plt.show()

plt.title("соответсвие номера и квадрата элемента из первой строки ")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(range(0,n),f[0],linestyle="-",color="g")

plt.show()