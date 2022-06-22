def inclusion(a, b):
    return set(a) ^ set(b)

a = list(map(int, input().split(sep=',')))
b = list(map(int, input().split(sep=',')))
print(inclusion(a, b))

