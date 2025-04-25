def find_common_elements(set1, set2):
    result = set()
    for el in set1:
        if el in set2:
            result.add(el)
    return result


def is_superset(set_a, set_b):
    is_true = True
    for el in set_b:
        if el not in set_a:
            is_true = False
            break
    return is_true


def remove_duplicates(items):
    return list(dict.fromkeys(items))


def count_unique_words(text):
    if (text.strip() == ''):
        return 0
    list_of_words = text.split(' ')
    list_of_words = map(lambda w: w.lower(), list_of_words)
    return len(set(list_of_words))


def find_shared_items(*sets):
    return sets[0].intersection(*sets[1::1])
