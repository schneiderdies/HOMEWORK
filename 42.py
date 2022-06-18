x = int(input('Введите положительное число: \n'))
c = 0
d = []
for i in range(2, x):
    if a % i == 0:
        d.append(i)
if len(d) == 0:
    print('-1')
else:
    for i in range(len(d)):
        print(d[i])
