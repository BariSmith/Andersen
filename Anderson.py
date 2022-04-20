'''1. Составить алгоритм: если введенное число больше 7,
 то вывести "Привет"'''

start_digit = input('Please write your digit:')
if start_digit == '7':
     print('Привет')
else:
    print("Uncorrect digit")

'''2. Составить алгоритм: если введенное имя совпадает с Вячеслав
, то вывести “Привет, Вячеслав”, если нет, 
то вывести "Нет такого имени"'''

name = input('Пожалуйста введите имя:')
if name == 'Вячеслав':
    print(f'Привет,{name}')
else:
    print("Нет такого имени")


'''3. Составить алгоритм: на входе есть числовой массив,
 необходимо вывести элементы массива кратные 3'''

digits_list = []
digits = input('pls write you digits: ').split(',')
digits_list.append(digits)
digits_list = tuple(digits_list)

for tuple in digits_list:
    for elem in tuple:
        elem = int(elem)
        if elem%3==0:
            print(elem)
        else:
            print('Число не делится нацело на 3')





