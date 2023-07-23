# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = abs(int(input('пожалуйста, введите число N ')))

stop_number = 0
count = 2
for i in range(N):
    if stop_number != 1:
        count = count ** i
        if count <= N:
            print(count, end=' ')
            count = 2
        else:
            stop_number = 1
    else:
        i = N