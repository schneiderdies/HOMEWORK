with open('sah_yktdt-ud-test.conllu.txt', encoding='utf-8') as f:
    s = []
    for line in f:
        if line[0] in '123456789':
            a = line.split()
            if a[3] == 'VERB':
                s.append(line.split()[1])
    b = sorted(set(s))
print('Введите название файла: ')
name = input()
c = open(name, 'w')
for i in b:
    c.write(i + '\n')
c.close()






