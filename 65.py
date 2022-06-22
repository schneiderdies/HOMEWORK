while True:
    with open('лог беседы.txt', 'a', encoding='UTF-8') as f:
        print('Как дела?')
        f.write('Как дела?' + '\n')
        a = input()
        f.write(a + '\n')




