from string import punctuation
text = input()
while text != 'отстань':
    a = dict()
    for sign in punctuation:
        a[sign] = 0
    for letter in text:
        if letter in punctuation and letter in a:
            a[letter] += 1
    print(a)
    text = input()