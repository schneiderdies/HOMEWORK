import json

a = []
b = []
c = []
with open("laureate.json", "r") as f:
    data = json.load(f)

for laureate in data['laureates']:
    for i in laureate['prizes']:
        if i['category'] == 'physics':
            a.append(laureate)
for laureate in a:
    if 'Germany' not in laureate['bornCountry']:
        b.append(laureate)
for laureate in b:
        i = laureate['prizes']
        for d in i:
            for x in d['affiliations']:
                if 'dict' in str(type(x)):
                    if 'country' in x.keys():
                        if 'Germany' in x['country']:
                            c.append(laureate['surname'])
print(c)


