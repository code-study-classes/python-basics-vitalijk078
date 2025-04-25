def calculate_distance(x, y):
    return y - x


def calculate_segments(a, b):
    return round(a // b)


def calculate_digit_sum(number):
    return sum(map(int, str(abs(number))))


def round_to_multiple(number, multiple):
    return multiple * round(number / multiple)


def calculate_rect_area(x1, y1, x2, y2):
    return abs(x2 - x1) * abs(y2 - y1)
