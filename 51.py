s1 = input()
s2 = input()
a = []
for t in s1.split():
    try:
        a.append(int(t))
    except ValueError:
        pass
b = []
for i in s2.split():
    try:
        b.append(int(i))
    except ValueError:
        pass
avg1 = sum(a) / len(a)
avg2 = sum(b) / len(b)
if avg1 > avg2:
    print("Студент 1")
else:
    print("Студент 2")
#не очень понятно, что делать, если средние баллы студентов равны; если нужно - могу доделать


