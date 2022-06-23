import csv
a = []
TotalHeight = 0
Counter = 0
NoHeight = 0
with open('SuperHeroes.txt', 'r', encoding='UTF-8', newline='',  errors='ignore') as file:
    reader = csv.DictReader(file)
    for row in reader:
        x = row.split(sep=';')
        if x[8] == 'bad' and x[3] == 'Human':
            if x[5] != '':
                Counter += 1
                TotalHeight += float(x[5])
                a.append(float(x[5]))
            else:
                NoHeight += 1
    sorted(a)
    T = len(a)
    if T % 2 != 0:
        med = a[(T-1) // 2]
    else:
        med = (a[T // 2] + a[(T // 2) - 1]) // 2
    print((TotalHeight + med*NoHeight)/(Counter + NoHeight))