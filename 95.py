import json
import operator
countries = dict()
with open("laureate.json", "r") as f:
    data = json.load(f)
for i in data['laureates']:
    for b, c in i.items():
        if b == 'bornCountry' and c not in countries.keys():
            countries[c] = 0
        elif b == 'bornCountry' and c in countries.keys():
            countries[c] += 1
m = sorted(countries.items(), key=operator.itemgetter(1), reverse=True)
m = m[0:10]
for j in m:
    print(j[0])

