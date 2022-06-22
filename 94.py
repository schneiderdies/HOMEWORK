from string import punctuation
def un(name):
    a = []
    b = []
    with open(name, 'r', encoding='UTF-8') as f:
        for line in f:
            sent = ''
            for word in line.split():
                if word[-1] not in punctuation:
                    sent += word + ' '
                elif word[-1] in punctuation and word[-1] not in '?.!':
                    sent += word[:-1:] + ' '
                if word[-1] in '!?.':
                    sent += word[:-1:]
                    a.append(sent)
                    sent = ''
        for x in a:
            b.append(set(x.split()))

    return b

print(un(input()))

