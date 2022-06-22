import random

def mix(word):
    a = []
    for i in word:
        a.append(i)
    g = a[1:-1]
    output = a[0]
    m = []
    while len(m) != len(g):
        n = random.randint(1, len(g))
        if n not in m:
            m.append(n)
    for j in m:
        output += g[j - 1]
    output += a[-1]
    return output

print(mix(input()))

