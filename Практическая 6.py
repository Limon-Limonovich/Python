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
matrix_1 = [[2, 4, 3, 6], [5, 7, 1, 5]]
matrix_2 = [[2, 9, 0, 2], [3, 4, 7, 6]]
answer_matrix = [[0] * len(matrix_1[0]) for _ in range(len(matrix_1))]
print(answer_matrix)
for row in range(len(matrix_1)):
    for el in range(len(matrix_1[0])):
        answer_matrix[row][el] = matrix_1[row][el] * matrix_2[row][el]
print(answer_matrix)
for row2 in answer_matrix:
    print(f"Сумма чисел в списке: {sum(row2)}")
    
# Задание 3
fruits = [['Banana', 'apple'], ['apricot', 'Avocado'], ['lime', 'lemon'], ['Mango', 'grapes']]
big_fruits = []
for row in fruits:
    for el in row:
        if el[0].isupper():
            big_fruits.append(el)
print(big_fruits)

# Задание 4
random_elements = [['toy', 'bee', 'cheese', 'ear'],
                   [False, 'word', '0110110', 10],
                   ['happiness', '(」°ロ°)」', 'luck', None],
                   ['car', '<- code ->', 4.7, True]]
for row in random_elements:
    for index, el in enumerate(row, start = 1):
        if index % 2 == 0:
            print(f"Индекс: {index}; Элемент: {el}")
            
# Задание 5
col_str = int(input("Введите количество строк: "))
col_stolb = int(input("Введите количество столбцов: "))
matrix = []
for i in range(col_str):
    znach_str = []
    for j in range(col_stolb):
        vvod = int(input(f"Введи Значение элемента [{i}][{j}]: \n"))
        znach_str.append(vvod)
    matrix.append(znach_str)
print(f"\nТвой двумерный массив: ")
for znach_str in matrix:
    print(znach_str)
