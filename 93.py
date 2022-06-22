def kratno(a, b)
    m = set()
    for i in a:
        if i % b == 0:
            m.add(i)
    return m

a = list(map(int, input().split()))
b = int(input())
print(kratno(a, b))

