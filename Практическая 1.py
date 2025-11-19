# Задание 1
m = ['круг', 0.25, 'квадрат', 'треугольник', 15, 'круг', 'овал', '10']
m.remove(0.25)
m.remove(15)
m.remove('10')
print(m)

#Задание 2
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
del abc[1:5]
print(abc)

# Задание 3
numbers = [1, 4, 2, 6, 3, 5]
numbers.sort()
print(numbers)
# Задание 4
mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]
mass.sort()
print(mass)
del mass [0:4]
print(mass)
mass.sort(reverse = True)
print(mass)

# Задание 5
nums_0 = []
nums_plus = []
nums_minus = []
sum1 = 0
sum2 = 0
nums_col = int(input("Введи количество чисел: "))
for i in range(nums_col):
    i += 1
    num = int(input(f"Введи {i} число: "))
    if num < 0:
        nums_minus.append(num)
        sum1 += num
    elif num == 0:
        nums_0.append("*")
    elif num > 0:
        nums_plus.append(num)
        sum2 += num
sr_arif = sum2 / len(nums_plus)
print(f"Кол-во звёзд {len(nums_0)}: {nums_0}")
print(nums_0)
print(nums_plus)
print(nums_minus)
print(sum1)
print(sr_arif)
