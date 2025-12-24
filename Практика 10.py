# Задание 1
def upper(t):
    for el in t:
        if el.isupper():
            print(el, end=' ')
upper('PriVet')

# Задание 2
def punct(txt):
    count = 0
    for el in txt:
        if el in ',?!.()':
            count += 1
    print(count)

# Задание 3
def create_cube(x, y):
    for i in range(y):
        print('*' * x)

# Задание 4
def double(txt):
    result = ''
    for el in txt:
        result += el * 2
    print(result)
