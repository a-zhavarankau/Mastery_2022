# List, Dict, Set, FrozenSet

## Exercises

### 1. Dict Merge

_Implement function block inside `main.py::dict_merge`_

#### Example

For

```(Python)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
```

the output should be

```(Python)
dict_merge(dict1, dict2) == {'Ten': 10, 'Twenty': 20, 'Thirty': 30,
                             'Forty': 40, 'Fifty': 50}
```

#### Test

```bash
# Run
python3 -m unittest -v tests.TestDictMerge
```

### 2. Lists Concatenation

_There is a bug in one line of the code in `main.py::list_concatenation`. Find it, fix it, and submit_

Given two lists `lst1` and `lst2`, your task is to return a list formed by the elements of `lst1` followed by the elements of `lst2`.

_Note: this is a bugfix task, which means that the function is already implemented but there is a bug in one of its lines. Your task is to find and fix it._

#### Example

For `lst1 = [2, 2, 1]` and `lst2 = [10, 11]`, the output should be
`solution(lst1, lst2) = [2, 2, 1, 10, 11]`.

#### Test

```bash
# Run
python3 -m unittest -v tests.TestListConcatenation
```

### 3. Two Teams

_Implement the missing code, denoted by ellipses in `main.py::two_teams'. You may not modify the pre-existing code._

There are some `students` standing in a row, each has some number written on their back.
The students are about to divide into two teams by counting off by twos:
those standing at the even positions (0-based) will go to team A, and those standing at the odd position will join the team B.

Your task is to calculate the difference between the sums of numbers written on the backs of the students
that will join team A, and those written on the backs of the students that will join team B.

#### Example

For `students = [1, 11, 13, 6, 14]`, the output should be `solution(students) = 11`.

Students with numbers `1`, `13` and `14` will join team A,
and students with numbers `11` and `6` will join team B.
Thus, the answer is `(1 + 13 + 14) - (11 + 6) = 11`.

#### Test

```bash
# Run
python3 -m unittest -v tests.TestTwoTeams
```

### 4. Remove Tasks

_Implement the missing code, denoted by ellipses in `main.py::remove_tasks'. You may not modify the pre-existing code._

Today is a good day: it's the `k`th year since you started to work at the company,
which means you have to have a party today.
In order to get home earlier and prepare for the jamboree, you need to get home early.
You decided to remove each `k`th tasks from your `todo` list, since today is your day and you can do whatever you please.

Given the list of task ids in your `todo` list, remove each `k`th task from it and return the list of remaining tasks.

#### Example

For `k = 3` and `todo = [1237, 2847, 27485, 2947, 1, 247, 374827, 22]`,
the output should be `solution(k, todo) = [1237, 2847, 2947, 1, 374827, 22]`.

#### Test

```bash
# Run
python3 -m unittest -v tests.TestRemoveTasks
```

### Test All

```bash
python3 -m unittest -v tests
```
