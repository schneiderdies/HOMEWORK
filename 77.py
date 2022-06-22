def palindrom(word):
    vow = 'аеоуиэыяёю'
    con = 'бвгджзйклмнпрстфхцчшщъь'
    opp = word[::-1]
    a = True
    for i in range(len(word)):
        if word[i] in vow:
            if opp[i] not in vow:
                b = False
        else:
            if opp[i] not in con:
                b = False
    return b


print(palindrom(input()))