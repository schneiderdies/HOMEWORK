f = open('enron_3000.txt', encoding='UTF-8')
f2 = open('otvet.txt', 'w', encoding='UTF-8')
ans = []
z = []
for line in f:
    if line[0] in '0123456789':
        a = line.split(sep=',')
        if a[3][0] == '"':
            j = a[3][11:-3:]
        else:
            j = a[3][12:-3:]
        z.append(a[4])
        if a[4] != '':
            if a[4][0] == '"':
                k = a[4][11:-3:]
            else:
                k = a[4][12:-3:]
        else:
            k = ' без адресата '
        if a[5] != '':
            ans.append('Письмо от ' + j + ' адресату ' + k + ' с заголовком ' + a[5] + ' отправлено ' + a[2])
        else:
            ans.append('Письмо от ' + j + ' адресату ' + k + ' без заголовка отправлено ' + a[2])
f.close()
for x in ans:
    f2.write(str(x) + '\n')
f2.close()

