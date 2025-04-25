def sum_even_digits(number):
    sum = 0
    for digit in str(abs(number)):
        if int(digit) % 2 == 0:
            sum += int(digit)
    return sum


VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']


def count_vowel_triplets(text):
    count = 0
    result = 0
    for letter in text:
        if letter.lower() in VOWELS:
            count += 1
        else:
            count = 0
        if count >= 3:
            result += 1
    return result


def find_fibonacci_index(number):
    if number == 1:
        return 1
    first = 1
    second = 1
    sum = 0
    i = 2
    while sum <= number:
        i += 1
        sum = first + second
        if sum == number:
            return i
        first = second
        second = sum
    return -1


def remove_duplicates(string):
    if string == '':
        return ''
    result = string[0]
    for i in range(1, len(string)):
        prev = string[i - 1]
        if string[i] != prev:
            result += string[i]
    return result
