while True:

    while True:
        try:
            first_number = float(input('Enter first numbetr: '))
            break
        except ValueError:
            print('Invalid input!')

    while True:
        try:
            operation = input('Enter the operation: ')
            if operation in ('+', '-', '*', '/'):
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid input!')

    while True:
        try:
            second_number = float(input('Enter second numbetr: '))
            if operation == '/' and second_number == 0:
                raise ZeroDivisionError
            break
        except ValueError:
            print('Invalid input!')
        except ZeroDivisionError:
            print('Invalid input! can\'t division on Zero')

    match operation:
        case '+':
            result = first_number + second_number
        case '-':
            result = first_number - second_number
        case '*':
            result = first_number * second_number
        case '/':
            result = first_number / second_number
        case _:
            result = None

    if result != None:
        print(result)
    else:
        print('Error: invalid input!')


    while True:
        try:
            decision = input('do you want continue (y / n): ')
            if decision in ('y', 'n'):
                break
            else:
                raise ValueError
        except ValueError:
            print('Error: invalid input!')
    if decision == 'n':
        break
