def total(a=5, *numbers, **phonebook):
    print('a', a)

    # iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)

    # iterate through all the items in dictionary
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560)


def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y


print(maximum(2, 3))


def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


print_max(3, 5)
print(print_max.__doc__)
