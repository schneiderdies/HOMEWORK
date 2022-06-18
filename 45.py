print("Введите две строки")
m = input()
n = input()
m1 = m.split()
n1 = n.split()
x = []
for i in range(len(m1)):
    for k in range(len(n1)):
        if m1[i] == n1[k] and i == k:
            x.append(m1[i])
print("Слов:", len(x))