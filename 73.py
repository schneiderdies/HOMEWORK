def numbconv(a):
    rom = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    arab = [1, 5, 10, 50, 100, 500, 1000]
    output = 0
    m = []
    for i in range(len(a)):
        m.append(arab[rom.index(a[i])])
    if m == sorted(m, reverse=True):
        output = sum(m)
    else:
        for i in range(len(m) - 1):
            if m[i] < m[i+1]:
                m[i] = int('-' + str(m[i]))
        output = sum(m)
    return output

print(numbconv(input()))


