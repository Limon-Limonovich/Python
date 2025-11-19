# Задание 1
ne_chet = []
chet = []
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for el in row:
        if el % 2 != 0:
            ne_chet.append(el)
        elif el % 2 == 0:
            chet.append(el)
    print(row, end = '\n')
print(f"Не чётные числа: {ne_chet}")
print(f'Кол-во чётных: {len(chet)}')

# Задание 2
