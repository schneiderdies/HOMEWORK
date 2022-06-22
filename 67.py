name = input()
with open(name, encoding='UTF-8') as f:
    k = 0
    a = []
    signs = ['+', '-', '=', '+=', '-=', '!=', '==', '>=', '<=']
    for line in f:
        k += 1
        x = line.split()
        for word in x:
            for s in signs:
                if s in word and len(word) > 2:
                    a.append(k)
                elif s in word and len(word) == 2 and word not in signs:
                        a.append(k)
if len(a) != 0:
    a = sorted(set(a))
    for x in a:
        print('Строчка ' + str(x) + ' - некрасивая')
else:
    print('ОК')



