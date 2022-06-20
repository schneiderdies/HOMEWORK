link = 'https://gutenberg.org/ebooks/135'
with open('lesmiserables.txt', encoding='utf-8') as f:
    a = []
    for line in f:
        words = line.split()
        for i in words:
            if i[0] in 'ÀÁAÄÈÉEÊËÌIÍÎÏÒOÓÔUÙÚÛÜY':
                a.append(i)
for i in a:
    print(i)
print(len(a))



