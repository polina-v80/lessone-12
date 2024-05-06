def print_params (a = 1, b = 'строка', c = True):
    print('a: ', a)
    print('b: ', b)
    print('c: ', c)
    print()

# Функция с параметрами по умолчанию:
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

# Распаковка параметров:
values_list = [2, 'ноль', False]
values_dict = {'a': 1, 'b': 'строка', 'c': True}

print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры:
values_list_2 = ['mama', 3]
print_params(*values_list_2, 42)

#  Примечание урока
# def append_to_list(item, list_my=None):
#   if list_my is None:
#     list_my = []
#   list_my.append(item)
#
# print(list_my)
