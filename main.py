first_number = int(input('Choose the first number '))
while True:
    action = input('Choose the action ')
    second_number = int(input('Choose the second number '))
    if action == '*':
        first_number *= second_number
        print('Result:', first_number)
    elif action == '/':
        first_number /= second_number
        print('Result:', first_number)
    elif action == '+':
        first_number += second_number
        print('Result:', first_number)
    elif action == '-':
        first_number -= second_number
        print('Result:', first_number)
    else:
        print('Error, wrong action')
        break
