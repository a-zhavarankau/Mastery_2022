matrix = [[1, 2],
          [3, 4],
          [5, 6],
          [7, 8]]

result_transposed = (list(i) for i in zip(*matrix))
print(list(list(item) for item in result_transposed))
