name = input()
with open(name, encoding='UTF-8') as f:
    a = 0
    b = 0
    for line in f:
        b += 1
        if len(line.strip()) > 79:
            print('Строчка ' + str(a) + ' - слишком длинная, в ней ' + str(len(line.strip())) + ' символов')
            break
        else:
            b = 1
    if b == 1:
        print('OK')



