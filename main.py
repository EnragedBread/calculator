from choose_from import choose_from_menu

first_num = int(input(f'What is the first number in your equation? ').strip())
second_num = int(input(f'What is the second number in your equation? ').strip())

methods = ['Add', 'Subtract', 'Multiply', 'Divide']
method = choose_from_menu(methods, 'What operator does your equation use? ')

if method == 'Add':
    print(f'{first_num + second_num}')
elif method == 'Subtract':
    print(f'{first_num - second_num}')
elif method == 'Multiply':
    print(f'{first_num * second_num}')
else:
    print(f'{first_num / second_num}')