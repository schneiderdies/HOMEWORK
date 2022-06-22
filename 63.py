import os

import re

subjects = ['Математика',
            'Русский язык',
            'Иностранный язык',
            'Информатика',
            'Физика',
            'Химия',
            'История',
            'Обществознание',
            'Биология',
            'География',
            'Литература']

link_to_program = 'https://www.hse.ru/ba/ling'
filename = 'data.txt'
os.system('curl -XGET ' + link_to_program + ' > ' + filename)

score = {}

file = open(filename, 'r')

for line in file.readlines():
    for subj in subjects:
        if subj in line:
            if subj not in score:
                score[subj] = -1
            if 'минимальный балл' in line.lower():
                x = [int(s) for s in re.findall(r'-?\d+\.?\d*', line)][-1]
                score[subj] = x
            break

output_file = open('exams.txt', 'w')

for subj in score:
    if score[subj] != -1:
        output_file.write(subj + ' --- ' + str(score[subj]) + '\n')
        print(subj, '---', score[subj])
    else:
        output_file.write(subj)
        print(subj + '\n')