name = input('Введите название файла: ')
a = input('camel или under? \n')
with open(name, encoding='UTF-8') as f:
    k = 0
    flag = True
    for line in f:
        k += 1
        if a == 'camel':
            for i in line.strip().split():
                if i[0].isupper() or '_' in i:
                    print('строка', k, 'не по camelcase')
                    flag = False
                    break
                elif a == 'under':
                    for i in line.strip().split():
                        if i[0].isupper():
                            print('строка', k, 'не по under_score')
                            flag = False
                            break
    if flag:
        print('ok')


