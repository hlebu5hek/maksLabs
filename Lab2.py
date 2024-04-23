'''
Натуральные числа.
Выводит на экран числа, убирая нечетные цифры в каждом
четном по порядку числе. Убранные цифры печать отдельно прописью.
'''
import re
dc_cifr = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'} #Словарь с цифрами
file_name = "text.txt" #Выбор файла
with open(file_name, 'r') as file:
    f = file.readlines()
    i = 0
    for gived_num in f:
        gived_num = gived_num.replace('\n', '')
        i += 1
        if re.match("^[0-9]+$", gived_num):
            print(gived_num)
            if(re.match("^[24680]+$", str(i)[-1])):
                cifrs = re.sub(r"[24680]", '', gived_num)
                if cifrs:
                    print(re.sub(r"[13579]", '', gived_num))
                    for j in cifrs:
                        print(dc_cifr[j], end='  ')
                    print()
            print()