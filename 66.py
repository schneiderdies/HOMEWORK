a = 0
for i in range(1, 7):
    name = str(i) + '.txt'
    with open(name, encoding='utf-8') as f:
        for line in f:
            a += len(line.split())
print(a // 6)




