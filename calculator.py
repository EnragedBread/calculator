class InvalidCalculateMethodError(Exception):
    pass

def calculate(method, first_num, second_num):
    if method == 'Add':
        solution = first_num + second_num
    elif method == 'Subtract':
        solution = first_num - second_num
    elif method == 'Multiply':
        solution = first_num * second_num
    elif method == 'Divide':
        solution = first_num / second_num
    else:
        raise InvalidCalculateMethodError

    return solution