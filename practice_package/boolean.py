def check_between_numbers(a, b, c):
    return a < b < c or a > b > c


def check_odd_three(n):
    return 99 < abs(n) < 1000 and abs(n) % 2


def check_unique_digits(n):
    return 99 < abs(n) < 1000 and len(set(str(n))) >= 3


def check_ascending_digits(n):
    return (100 <= abs(n) <= 999) and \
        (abs(n) // 100 < abs(n) // 10 % 10 < abs(n) % 10)


def check_palindrome_number(n):
    return str(abs(n))[::-1] == str(abs(n))
