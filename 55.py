sent = input()
a = 0
b = len(sent.split())
for i in sent:
    if i in ":;?,!.":
        a = a + 1
c = round((a / b) * 100, 2)
print("Всего слов: ",b, ", со знаками: ", a, ", доля: ", c, "%")
