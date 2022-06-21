f = open('my_files.txt', 'rt')
a = []
for line in f:
    b = line.strip()
    if b[-3::] == '.py':
        line = line.replace('\t', ' ')
        a.append(line)
f.close()
f = open('my_files.txt', 'w')
for i in a:
    f.write(i)
f.close()

