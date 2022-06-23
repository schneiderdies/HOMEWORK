import json
import  operator
from string import punctuation
p = punctuation.replace('\'', '')
p = p.replace('-','')
p = p + '(' + ')'
a = []
f = dict()
with open('song.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        for word in line.split():
            word = word.lower()
            for sign in p:
                if sign in p and sign in word:
                    word = word.replace(sign, '')
            a.append(word)
for word in a:
    if word != '—' and word != '-':
        if word not in f:
            f[word] = 1
        else:
            f[word] += 1
f = dict(sorted(f.items(), key=operator.itemgetter(1), reverse=True))
output = dict()
c = 0
for i, j in f.items():
    output[i] = j
    c += 1
    if c == 10:
        break
with open('song_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(output, file,  ensure_ascii=False)

