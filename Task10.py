n = int(input('пожалуйста, напишите количество монет '))

eagle = 0
tails = 0

for i in range(n):
    x = int(input('орел(1) или решка(0)? '))
    if x == 1:
        eagle += 1
    else:
        tails += 1
if eagle < tails:
    print(f'переверните {eagle} монет с орла на решку')
elif eagle == tails:
    print(f'одинаковое количество орлов и решек, {eagle}')
else:
    print((f'переверните {tails} монет с решки на орла'))
