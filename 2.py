from itertools import groupby

dict_list = [
    {"key1": "value1"},
    {"k1": "v1", "k2": "v2", "k3": "v3"},
    {},
    {},
    {"key1": "value1"},
    {"key1": "value1"},
    {"key2": "value2"}
]


def my_func(my_dict):
    new_dict = [i for i, _ in groupby(my_dict)]
    return print(new_dict)


if __name__ == '__main__':
    my_func(dict_list)
