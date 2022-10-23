array_with_duplicates = [2, 2, 3, 1, 3]
non_repeated = []
for number in array_with_duplicates:
    if number not in non_repeated:
        non_repeated.append(number)
    else:
        non_repeated.remove(number)
print(*non_repeated)
