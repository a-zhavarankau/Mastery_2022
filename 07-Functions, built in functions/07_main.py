from typing import List, Union, Dict, Any


def custom_sum(array: List[Union[int, float]]) -> Union[int, float]:
    sum_of_nums: Union[int, float] = 0  # Types are defined according to mypy requirements
    for digit in array:
        sum_of_nums += digit
    return sum_of_nums


def custom_sort(array: List[int], reverse: bool = False) -> List[int]:
    result = []
    if len(array) == 1:
        return array
    mid = len(array) // 2

    left_part = custom_sort(array[:mid])
    right_part = custom_sort(array[mid:])

    x, y = 0, 0
    while x < len(left_part) and y < len(right_part):
        if left_part[x] > right_part[y]:  # < for descending
            result.append(right_part[y])
            y = y + 1
        else:
            result.append(left_part[x])
            x = x + 1

    result = result + left_part[x:]
    result = result + right_part[y:]

    if reverse is False:
        return result
    else:
        result.reverse()
        return result


def dict_factory(*args, default_=None, **kwargs) -> Dict[Any, Any]:
    return {k: default_ for k in args} | kwargs


def lambda_message_factory(msg):
    return lambda *arg, **kwarg: msg.format(*arg, **kwarg)
