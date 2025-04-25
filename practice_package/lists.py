import re


def square_odds(numbers):
    filtered_numbers = filter(lambda a: a % 2 != 0, numbers)
    return list(map(lambda a: a ** 2, filtered_numbers))


def normalize_name(name):
    if name == '':
        return ''
    result = name.lower()
    result = result[0].upper() + result[1::1]
    return result


def normalize_names(names):
    return list(map(normalize_name, names))


def is_email_invalid(email):
    return len(email) >= 5 and re.fullmatch(r'^[^@]+@[^@]+$', email)


def remove_invalid_emails(emails):
    return list(filter(is_email_invalid, emails))


def filter_palindromes(words):
    return list(filter(lambda w: w.lower()[::-1] == w.lower(), words))


def calculate_factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(0, n):
        print(i)
        result *= i + 1
    return result


def find_common_prefix(strings):
    if len(strings) == 1:
        return strings[0]
    result = strings
    result_len = len(result)
    prefix = ''
    i = 0
    while len(result) == result_len:
        previous_prefix = prefix
        prefix = result[0][0:i:1]
        result = list(filter(lambda w: prefix in w, result))
        i += 1
        if i > len(result[0]) + 1:
            break
    return previous_prefix
