def trans(word):
    rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    eng = ['a', 'b', 'v', 'g', 'd', 'e', 'yo', 'zh', 'z', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'sch', 'y', 'e', 'yu', 'ya']
    translit = ''
    for i in word:
        translit += eng[rus.index(i)]
    return translit
print(trans(input()))


