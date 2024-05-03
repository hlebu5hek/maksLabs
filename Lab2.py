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
    for i, gived_num in enumerate(f):
        gived_num = gived_num.replace('\n', '')
        print(gived_num)
        if re.match("^[0-9]+$", gived_num) and i%2==0:
            cifrs = re.sub(r"[24680]", '', gived_num)
            if cifrs:
                print(cifrs)
                for j in cifrs:
                    print(dc_cifr[j], end='  ')
                print()
        print()