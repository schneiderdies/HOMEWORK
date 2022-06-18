a = [int(x) for x in input().split()]
s = sum(a) / len(a)
ans = sorted([x for x in a if s - 1 <= x <= s + 1])
print(len(ans))
for x in ans:
    print(x, end=' ')
