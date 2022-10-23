# Functions, Build in Functions

## Exercises

### 1. Custom `sum` Function

_Implement `custom_sum` function inside the `main.py` file_

Need to implement `custom_sum` function without using built-in `sum` function.
Function must accept list of argument and return sum of lists elements regarding rules below:

- If the list contains only integer numbers, the function should return an integer value
- Otherwise, float value

#### Input/Output

- [input] List[Union[int, float]]
- [output] Union[int, float]

#### Examples:

- For `l = [1, 2, 3, 4]`, the output should be `custom_sum(l) = 10`.
- For `l = [1, 2, 3.4]`, the output should be `custom_sum(l) = 6.4`.

#### Test

```bash
# Run
python3 -m unittest -v tests.TestCustomSum
```


### 2. Custom `sort` Function

_Implement `custom_sort` function inside the `main.py` file_

Need to implement `custom_sort` function without using built-in `sorted` function and `.sort` method.
Function must accept list of integers and `reverse` boolean value as argument and return sorted list regarding rules below:

- If `reverse = False` return list of arguments in ascending order
- If `reverse = True` return list of arguments in descending order.
- `reverse` is optional and by default is `False`

#### Input/Output

- [input] List[int]
- [output] List[int]

#### Examples:

- For `l = [3, 2, 5, 1, 4]` and `reverse = False`, the output should be `custom_sort(l, reverse) = [1, 2, 3, 4, 5]`
- For `l = [3, 2, 5, 1, 4]` and `reverse = True`, the output should be `custom_sort(l, reverse) = [5, 4, 3, 2, 1]`
- For `l = [3, 2, 5, 1, 4]`, the output should be `custom_sort(l) = [1, 2, 3, 4, 5]`

#### Test

```bash
# Run
python3 -m unittest -v tests.TestCustomSort
```

### 3. Dict Factory

_Implement `dict_factory` function inside the `main.py` file_

Need to implement a function that can accept an infinite amount of arguments
including keyword arguments and return dict object with these arguments.
Keyword argument should be `key=value` row in dict.
Single argument should be `key=<default_>` row in dict, where `<default_>` is a value of the function argument (`func(..., default_=<value>)`).
`default_` can be optional with `None` value.

#### Examples:

```python
# With `default_` as 'def'
>>> dict_factory('k1', 'k2', k3='v3', k4='v4', default_='def')
{
    'k1': 'def',
    'k2': 'def',
    'k3': 'v3',
    'k4': 'v4',
}

# Without `default_`
>>> dict_factory('k1', 'k2', k3='v3', k4='v4')
{
    'k1': None,
    'k2': None,
    'k3': 'v3',
    'k4': 'v4',
}
```

#### Test

```bash
# Run
python3 -m unittest -v tests.TestDictFactory
```



### 4. Lambda Message Factory*

_Implement `lambda_message_factory` function inside the `main.py` file_

Need to implement a function that will return lambda object which will return custom message,
regarding function template.

#### Examples:

```python
>>> lambda_msg_one = lambda_message_factory('Hello, my name is {name}!')
>>> lambda_msg_two = lambda_message_factory('Wow! Such {such}. So {}')

>>> lambda_msg_one(name='Monty')
'Hello, my name is Monty!'

>>> lambda_msg_two('agile', such='python')
'Wow! Such python. So agile'
```

#### Test

```bash
# Run
python3 -m unittest -v tests.TestLambdaMessageFactory
```
