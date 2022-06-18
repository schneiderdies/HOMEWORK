sent = input()
x = sent.split()
line = ''
for word in x:
    if word[0].islower() or word == x[0]:
        line += word + ' '
    elif word[0].isupper():
        if word[-1] == '.':
            line += 'NAME.'
        elif word[-1] == ',':
            line += 'NAME, '
        elif word[-1] == '!':
            line += 'NAME!'
        elif word[-1] == '?':
            line += 'NAME?'
        else:
            line += 'NAME '
print(line)
