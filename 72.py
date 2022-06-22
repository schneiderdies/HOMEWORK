def vowscons(name):
    vows = 'eyuioaуеыаоэяиюё'
    cons = 'qwrtpsdfghjklzxcvbnmйцкнгшщзхфвпрлджчсмтб'
    vow = 0
    con = 0
    with open(name, encoding='utf-8') as f:
        for line in f:
            for i in line:
                if i in vows:
                    vow += 1
                if i in cons:
                    con += 1
    c = 'В файле ' + name + ' ' + str(vow) + ' гласных и ' + str(con) + ' согласных.'
    return c
print(vowscons(input()))

