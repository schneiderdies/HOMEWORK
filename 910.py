import csv
import json
inp = {}
inp['a'] = []
name = input('Введите название файла: ')
with open(str(name + '.csv'), 'r', encoding='UTF-8') as csvf:
    reader = csv.DictReader(csvf)
    for row in reader:
        inp['a'].append(row)
with open(str(name + '.json'), 'w', encoding='UTF-8') as jf:
    json.dump(inp, jf, ensure_ascii=False)


