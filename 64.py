try:
    with open('kartowka.txt', 'r', encoding='utf-8') as f:
        a = 0
        for line in f:
            a += 1
        print(a)
except I0Error:
    print("Файл недоступен")



