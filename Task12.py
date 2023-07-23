x = abs(int(input('пожалуйста, напишите натуральное число X ')))
y = abs(int(input('пожалуйста, напишите натуральное число Y ')))

if x < 1 or x > 1000 or y < 1 or y > 1000:
    print('введенное число находится не в диапазоне <=1000')
else:
    S = x + y
    P = x * y
    stop = 0
    for i in range(1001):
        if stop != 1:
            for j in range(1001):
                if stop != 1:
                    if i * j == P and i + j == S:
                        print(i, j)
                        stop = 1
            else:
                j = 1001
        else:
            i = 1001