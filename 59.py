link = 'https://gutenberg.org/ebooks/135'
with open('lesmiserables.txt', encoding='utf-8') as f:
    a = []
    b = 0
    for line in f:
        words = line.split()
        for j in words:
            if j[-1] in '?!.':
                b = b + 1
print(b)




