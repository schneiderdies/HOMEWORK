a = int(input('Введите положительное число: \n'))
en = 0
on = 0
while a != 0:
    if a % 10 != 0:
        if (a % 10) % 2 == 0:
            en += 1
        else:
            on += 1
    a //= 10
print('количество чётных цифр: ', en)
print('количество нечётных цифр: ', on)
