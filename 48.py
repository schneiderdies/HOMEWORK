n = int(input())
mult = 1
while n > 0:
    m = n % 10
    mult = mult * m
    n = n // 10
print("Произведение: ", mult)
