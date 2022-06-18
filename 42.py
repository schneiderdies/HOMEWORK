a = input().split()
print(a[0], end = '')
for i in range(1, len(a)):
    print(" ", end = '')
    if ord(a[i][0]) >= ord('А') and ord(a[i][0]) <= ord('Я'):
        print("NAME", end = '')
    else:
        print(a[i], end = '')