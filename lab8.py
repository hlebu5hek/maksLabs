'''Объекты – отрезки
Функции:
сегментация
визуализация
проверка пересечения
зеркальное отражение относительно заданной оси
'''

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Students")
root.geometry('840x512')
root.resizable(False, False)

canv = Canvas(root, width=400, height=400, bg="white", cursor="pencil", )
canv.create_line(0, 200, 400, 200, width=1)
canv.create_line(200, 0, 200, 400, width=1)

lines = []


class line():
    x1, x2, y1, y2 = 0, 0, 0, 0

    def __init__(self, _x1, _y1, _x2, _y2):
        if _x1 < _x2:
            self.x1 = _x1
            self.x2 = _x2
            self.y1 = _y1
            self.y2 = _y2
        else:
            self.x1 = _x2
            self.x2 = _x1
            self.y1 = _y2
            self.y2 = _y1


def segment(ls = lines):
    canv.delete('all')
    canv.create_line(0, 200, 400, 200, width=1)
    canv.create_line(200, 0, 200, 400, width=1)
    for i in ls:
        canv.create_line(i.x1 * 10 + 200, i.y1 * 10 + 200, i.x2 * 10 + 200, i.y2 * 10 + 200, width=1, dash=int(entrys.get()))


def check_intersection(l1, l2):
    dx1 = l1.x2 - l1.x1
    dx2 = l2.x2 - l2.x1
    dy1 = l1.y2 - l1.y1
    dy2 = l2.y2 - l2.y1

    k1 = dy1 / dx1
    k2 = dy2 / dx2

    b1 = l1.y1 - k1 * l1.x1
    b2 = l2.y1 - k2 * l2.x1

    if k1 == k2: return [False, 0, 0]

    x = (b2 - b1) / (k1 - k2)
    y = k1 * x + b1

    if (l1.x1 <= x <= l1.x2) and (l2.x1 <= x <= l2.x2): return [True, x, y]

    return [False, 0, 0]


def find_intersections():
    for i in range(len(lines)):
        for j in range(i, len(lines)):
            res = check_intersection(lines[i], lines[j])
            if res[0]:
                x = res[1]
                y = res[2]
                canv.create_line(x*10+199, y*10+199, x*10+201, y*10+201, width=10, fill='red')


def mirror_by_axis():
    global lines

    ax = entryax.get()
    value = int(entryv.get())
    lines_n = []

    if (ax == 'y'):
        for i in lines:
            l = line(value - i.x1, i.y1, value - i.x2, i.y2)
            lines_n.append(l)
    else:
        for i in lines:
            l = line(i.x1, value - i.y1, i.x2, value - i.y2)
            lines_n.append(l)

    linesList_n = []
    for i in lines_n:
        linesList_n.append(str(i.x1) + ';' + str(i.y1) + ' : ' + str(i.x2) + ';' + str(i.y2) + '\n')

    draw_lines(lines_n)
    PrintList(linesList_n)

    lines = []
    lines.extend(lines_n)


def load_lines():
    lineList = []
    filename = entryf.get()

    with open(filename, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            a = i.split(' ')
            l = line(int(a[0]), int(a[1]), int(a[2]), int(a[3]))
            lines.append(l)
            lineList.append(a[0] + ';' + a[2] + ' : ' + a[1] + ';' + a[3] + '\n')

    PrintList(lineList)
    draw_lines(lines)


def PrintList(list):
    studListd = StringVar(value=list)
    listboxd = Listbox(listvariable=studListd)
    listboxd.place(anchor=NW, x=15, y=65, width=385, height=360)

    scrollbar = ttk.Scrollbar(orient="vertical", command=listboxd.yview)
    scrollbar.place(anchor=NW, y=65, x=385, width=20, height=360)
    listboxd["yscrollcommand"] = scrollbar.set


def draw_lines(ls):
    canv.delete('all')
    canv.create_line(0, 200, 400, 200, width=1)
    canv.create_line(200, 0, 200, 400, width=1)
    for i in ls:
        canv.create_line(i.x1 * 10 + 200, i.y1 * 10 + 200, i.x2 * 10 + 200, i.y2 * 10 + 200, width=1)


# tkinter
btn = ttk.Button(text="Загрузить из файла", command=load_lines)
btn.place(anchor=NW, x=250, y=20, height=25, width=150)

btn1 = ttk.Button(text="Сегментация", command=segment)
btn1.place(anchor=NW, x=15, y=432, height=25, width=100)

btn2 = ttk.Button(text="Пересечения", command=find_intersections)
btn2.place(anchor=NW, x=300, y=432, height=25, width=100)

btn3 = ttk.Button(text="Отражение", command=mirror_by_axis)
btn3.place(anchor=NW, x=720, y=432, height=25, width=100)

labelFile = ttk.Label(text="Имя файла:")
labelFile.place(anchor=NW, x=15, y=20, height=25)
entryf = ttk.Entry()
entryf.place(anchor=NW, x=90, y=20, height=25, width=150)

labelax = ttk.Label(text="Ось для отражения:")
labelax.place(anchor=NW, x=429, y=470, height=25)
entryax = ttk.Entry()
entryax.place(anchor=NW, x=559, y=470, height=25, width=40)

labelv = ttk.Label(text="Значение для отражения:")
labelv.place(anchor=NW, x=624, y=470, height=25)
entryv = ttk.Entry()
entryv.place(anchor=NW, x=779, y=470, height=25, width=40)

labels = ttk.Label(text="Значение для сегменнтации:")
labels.place(anchor=NW, x=15, y=470, height=25)
entrys = ttk.Entry()
entrys.place(anchor=NW, x=190, y=470, height=25, width=40)

studListd = StringVar(value=[])
listboxd = Listbox(listvariable=studListd)
listboxd.place(anchor=NW, x=15, y=65, width=385, height=360)

scrollbar = ttk.Scrollbar(orient="vertical", command=listboxd.yview)
scrollbar.place(anchor=NW, y=65, x=385, width=20, height=360)
listboxd["yscrollcommand"] = scrollbar.set

canv.place(x=420, y=15)
root.mainloop()
