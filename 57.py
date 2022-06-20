link = 'https://gutenberg.org/ebooks/135'
with open('lesmiserables.txt', encoding='utf-8') as f:
    c = 1
    len_text = 0
    for line in f:
        words = len(line.split())
        len_text += words
        print('В строке ' + str(c) + ' содержится слов ' + str(words))
        c = c + 1
print(len_text)





