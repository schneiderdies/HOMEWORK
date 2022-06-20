x = input()
a = []
for t in x.split():
    try:
        a.append(int(t))
    except ValueError:
        pass
b = sorted(a)
m = len(b)
n = 0
if len(b) % 2 != 0:
    n = a[m // 2]
else:
    n = (a[(m//2)-1] + a[m//2])/2
print(float(n))

