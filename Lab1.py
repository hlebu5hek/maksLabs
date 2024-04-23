'''
Натуральные числа.
Выводит на экран числа, убирая нечетные цифры в каждом
четном по порядку числе. Убранные цифры печать отдельно прописью.
'''
#Словарь с цифрами
dc_cifr = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}
#Баффер
gived_num = '1'
#Выбор файла
file_name = "text.txt"
#Номер числа по порядку
i = 0

try:
    open(file_name, 'r')
except:
    print('Файл отсутствует в директории проекта')
    exit()

with open(file_name, 'r') as file:
    while 1:
        i+=1
        gived_num = file.readline().replace('\n', '')
        if not gived_num:
            #print('Файл закончился')
            break
        if not gived_num.isdigit():
            continue

        print()
        print(gived_num)
        cutted =  ''

        if i % 2 == 0:
            for j in gived_num:
                if int(j) % 2 == 0:
                    cutted += j
            if cutted == gived_num:
                continue

            print(cutted)

            for j in gived_num:
                if int(j) % 2 != 0:
                    print(dc_cifr[j], end='  ')
            print()