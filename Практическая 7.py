# Задание 1
data = [['folder', 'coursework.doc', 'folder', 'pict.png', 'data.accdb'],
        ['icon.ico', 'script.js', 'index.html', 'style.css', 'prog.py'],
        ['my_song.mp3', 'anapa-2003.jpg', 'cs_1.6.exe', 'folder', 'cheat.txt'],
        ['notes.txt', 'main.py', 'work.pdf', 'cartoon.mp4', 'array.py'],
        ['project.psd', 'cycle.py', 'folder', 'cycle.js', 'turtle.py']]
data_notPy = []
data_notjs = []
for row in data:
    new_data = []
    for el in row:
        if el == 'folder':
            continue
        elif el == 'data.accdb':
            new_data.append('data.sql')
        else:
            new_data.append(el)

        if el[-3::] == '.py':
            data_notPy.append(el)
        if el[-3::] == '.js':
            data_notjs.append('new_' + el)

    print(new_data)
print(f"\nЭлементы с расширения .py:\n{data_notPy}")
print(f"\nЭлементы с расширения .js:\n{data_notjs}")

# Задание 2
word_numb = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
n = int(input("Введите число от 0 до 9: "))
if n >= 0 and n <= 9:
    for i in range(n + 1):
        print(f"{word_numb[i]}")
else:
    print("Введите число <= 9")
# Задание 3

# Задание 4
a = [[-446, 281, - 80], [465, 432, -122], [13, "error", 8]]
for index_i, row in enumerate(a):
    for index_j, el in enumerate(row):
        print(f"Индекс: {index_i, index_j} Элемент: {el}")
        if isinstance(el, str):
            a[index_i][index_j] = len(el)
print(a)

# Задание 5
matrix = [[1, 10, 11],
          [100, 101, 110],
          [111, 1000, 1001]]
summ = 0
for index_i, row in enumerate(matrix):
    for index_j, el in enumerate(row):
        if matrix[0][0] == el:
            summ += el
        elif matrix[1][1] == el:
            summ += el
        elif matrix[2][2] == el:
            summ += el
print(summ)
