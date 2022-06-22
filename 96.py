import json
died = dict()
pw = dict()
a = []
with open("laureate.json", "r") as f:
    data = json.load(f)
for i in data['laureates']:
    for b, c in i.items():
        if b == 'surname':
            died[i[b]] = i['died']
            pw[i[b]] = ''
for i in data['laureates']:
    for b, c in i.items():
        for j, k in pw.items():
            if c == j:
                for l in i['prizes']:
                    pw[j] = l['year']
for j, k in pw.items():
    for d, e in died.items():
        if d == j:
            if int(e[:4])  == int(k) + 1 or int(e[:4])  == int(k):
                a.append(d)
for j in a:
    print(d)

