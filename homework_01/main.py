"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num * num for num in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(x):
    if x > 1 and all(x % i for i in range(2, x)): # 1 не является простым числом
        return x


def filter_numbers(*args):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
            
    if args[-1] == 'odd':
        return list(filter(lambda num: num % 2 != 0, args[0]))
    elif args[-1] == 'even':
        return list(filter(lambda num: num % 2 == 0, args[0]))
    elif args[-1] == 'prime':
        return list(filter(is_prime, args[0]))


print(power_numbers(1, 2, 5, 7))