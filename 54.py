word = input()
a = []
while word != "":
    if word[-3:-1] == "eb":
        a.append(word)
    word = input()
for i in sorted(a):
    print(i)

