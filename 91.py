def intersec(a, b, isUnion):
    if isUnion:
        c = set(a) | set(b)
    else:
        c = set(a).intersection(b)
    return c
a = list(map(int, input().split(sep=',')))
b = list(map(int, input().split(sep=',')))
isUnion = input()
if isUnion == 'False':
    isUnion = False
else:
    isUnion = True
print(intersec(a, b, isUnion))

