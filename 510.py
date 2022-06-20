with open('pg66655.txt', encoding='utf-8') as f:
    text = f.read()
    par = text.split('\n\n')
    a = 0
    for i in range(len(par)):
        if 'A STORY ABOUT MYSELF.' in par[i]:
            a = i
    par = par[a::]
    b = []
    for j in par:
        b.append(j.split())
    c = 0
    for j in b:
        c = c + len(j)
print(int(c/len(par)))






