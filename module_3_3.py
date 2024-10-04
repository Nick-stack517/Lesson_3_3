def print_params(a=1, b='строка', c=True):
    # print(a, b, c)
    if type(a) == list:
        print(*a, b, c)

    else:
        print(a, b, c)


print('1.Функция с параметрами по умолчанию: ')
# print('1.Функция с параметрами по умолчанию: \n')
print_params(1, 'R', False)
print_params(1, 'R')
print_params(1, )
print_params()

print_params(b=25)
print_params(c=[1, 2, 3])

print()
print('2.Распаковка параметров:')

values_list = [[4, 'October'], 1957, True]
values_dict = {'a': 7, 'b': 'november', 'c': True}

print_params(*values_list)
print_params(**values_dict)

print()
print('3.Распаковка + отдельные параметры:')

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
