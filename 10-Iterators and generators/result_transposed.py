matrix = [[1, 2],
          [3, 4],
          [5, 6],
          [7, 8]]


def inner_gen(item, matrix):
    for elem in range(len(matrix)):
        yield matrix[elem][item]


def transpose(matrix):
    for item in range(len(matrix[0])):
        yield inner_gen(item, matrix)


gen = transpose(matrix)

for item in gen:
    for elem in item:
        print(elem)
