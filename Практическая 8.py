# Задание 1
my_dict = {1:'0101101', 2:'101110', 3:'1A14C', 4:'1100100', 5:'101010'}
print(my_dict)
del my_dict[3]
print(my_dict)
my_dict[10] = '0100101'
print(my_dict)

# Задание 2
sl = {'</>':13, 'script':1, '__init__':10, 'self':5, 'number_9':6, '#comment':100}
print(sl)
v = input("Введи значение для ключа")
k = input("Введи название ключа")
sl[k] = [v]
print(sl)
