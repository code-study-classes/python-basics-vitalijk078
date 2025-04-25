def count_char_occurrences(text):
    result = {}
    for letter in text:
        if (letter.lower() != letter.upper()):
            if letter.lower() in result.keys():
                result[letter.lower()] += 1
            else:
                result[letter.lower()] = 1
    return result


def merge_dicts(dict1, dict2, conflict_resolver):
    result = dict1
    for key in dict2:
        if key in result.keys():
            result[key] = conflict_resolver(key, dict1[key], dict2[key])
        else:
            result[key] = dict2[key]
    return result


def invert_dictionary(original_dict):
    result = {}
    for key in original_dict:
        if original_dict[key] in result.keys():
            result[original_dict[key]].append(key)
        else:
            result[original_dict[key]] = [key]
    return result


def get_columns_length(data_dict, columns):
    columns_length = {}
    for column in columns:
        for value in data_dict.values():
            if column in value.keys():
                if column in columns_length.keys():
                    if (columns_length[column] < len(str(value[column]))):
                        columns_length[column] = len(str(value[column]))
                else:
                    if len(str(value[column])) < 3:
                        columns_length[column] = 3
                    else:
                        columns_length[column] = len(str(value[column]))
    return columns_length


def dict_to_table(data_dict, columns):
    columns_length = get_columns_length(data_dict, columns)

    head = '|'
    stick = '|'
    for column in columns:
        head += \
            f' {column.upper()}{" " * (columns_length[column] - len(column))} |'
        stick += \
            f'{"-" * (columns_length[column] + 2)}|'
    result = f'{head}\n{stick}'

    for value in data_dict.values():
        row = '\n|'
        for column in columns:
            if column in value.keys():
                indent = columns_length[column] - len(str(value[column]))
                row += \
                    f' {value[column]}{" " * indent} |'
            else:
                indent = columns_length[column] - 3
                row += \
                    f' N/A{" " * indent} |'
        result += row
    return result


def deep_update(base_dict, update_dict):
    result = {}
    for key in base_dict:
        if key in update_dict.keys():
            if type(base_dict[key]) is dict and type(update_dict[key]) is dict:
                result[key] = deep_update(base_dict[key], update_dict[key])
            else:
                result[key] = update_dict[key]
        else:
            result[key] = base_dict[key]
    return result
