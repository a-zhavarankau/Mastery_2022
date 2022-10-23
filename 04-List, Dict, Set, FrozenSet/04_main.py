def dict_merge(dict1, dict2):
    return dict1 | dict2


def list_concatenation(lst1, lst2):
    res = lst1
    res.extend(lst2)
    return res


def two_teams(students):
    return sum(students[::2]) - sum(students[1::2])


def remove_tasks(k, todo):
    del todo[k - 1::k]
    return todo
