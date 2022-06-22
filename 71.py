def func(a, b, c):
    sum_true = 0
    sum_false = 0
    if c:
        for i in range(a, b + 1):
            if i % 2 == 0:
                sum_true += 1
        return sum_true
    elif not c:
        for i in range(a, b + 1):
            if i % 2 != 0:
                sum_false += i
        return sum_false


print("Введите границы промежутка: ")
a, b = map(int, input().split())
print('Число чётное или нечётное?')
x = input()
if x == "чётное" or x == "четное":
    c = True
elif x == "нечётное" or x == '' or x == "нечетное":
    c = False
print(func(a, b, c))
