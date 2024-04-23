'''Вариант 18
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N),
состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется
случайным образом целыми числами в интервале [-10,10].
Для тестирования использовать не случайное заполнение, а целенаправленное.
d e
c b
 4
3 1
 2
Формируется матрица F следующим образом:
если в С количество чисел, больших К в нечетных столбцах в области 3 больше,
чем произведение чисел в нечетных строках в области 2,
то поменять в В симметрично области 1 и 3 местами,
иначе С и Е поменять местами несимметрично.
При этом матрица А не меняется. После чего вычисляется выражение:
((К*A)*F+ K* F T . Выводятся по мере формирования А, F и
все матричные операции последовательно.
'''

from random import randint as rnd

def printList(z):
    for i in z:
        for j in i:
            print("{:5}".format(j), end=' ')
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
for i in range(m//2):
    for j in range(0, i+1):
        if j % 2 == 0: continue
        count_ += 1 if c[i][j] > k else 0
for i in range(m//2, m):
    for j in range(0, m-i):
        if j % 2 == 0: continue
        count_ += 1 if c[i][j] > k else 0
print("В С количество чисел, больших К в нечетных столбцах в области 3 = ", count_)

mult_ = 1
for j in range(m//2):
    for i in range(m-j-1, m):
        if i % 2 == 0: continue
        mult_ *= c[i][j]
for j in range(m//2, m):
    for i in range(j, m):
        if i % 2 == 0: continue
        mult_ *= c[i][j]
print("В С произведение чисел в нечетных строках в области 2 = ", mult_)


if count_ > mult_:
    print("Количество чисел, больших К, больше произведения\n")
    for i in range(0, m//2):
        for j in range(0, i+1):
            b[i][j], b[i][m-j-1] = b[i][m-j-1], b[i][j]
    for i in range(m//2, m):
        for j in range(0, m-i-1):
            b[i][j], b[i][m-j-1] = b[i][m-j-1], b[i][j]
else:
    print("Количество чисел, больших К, меньше произведения\n")
    for i in range(m):
        for j in range(m):
            c[i][j], e[i][j] = e[i][j], c[i][j]

print("Матрица B : ")
printList(b)
print("Матрица C : ")
printList(c)
print("Матрица D : ")
printList(d)
print("Матрица E : ")
printList(e)

f = []
f.extend(d)
f.extend(c)
for i in range(m):
    f[i].extend(e[i])
for i in range(m, n):
    f[i].extend(b[i-m])

print("Матрица F : ")
printList(f)

ak = []
for i in range(n):
    ak.append([])
    for j in range(n):
        ak[i].append(a[i][j] * k)

print("Матрица A умноженная на K : ")
printList(ak)

fa = []

for i in range(n):
    fa.append([])
    for j in range(n):
        s = 0
        for l in range(n):
             s += f[i][l]*ak[j][l]
        fa[i].append(s)

print("Матрица F умноженная на A*K : ")
printList(fa)

ft = []

for i in range(n):
    ft.append([])
    for j in range(n):
        ft[i].append(f[j][i])

print("Матрица F трансп. : ")
printList(ft)

for i in range(n):
    for j in range(n):
        ft[i][j] *= k

print("Матрица F трансп. умноженная на K : ")
printList(ft)

for i in range(n):
    for j in range(n):
        ft[i][j] += fa[i][j]

print("((К * A) * F + K * FT : ")
printList(ft)