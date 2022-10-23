# Iterators and generators

## Exercises

### 1.
Write generator expressions to generate sequences like "PPP", "YYY", "TTT", "HHH", "OOO", "NNN".  
Write generator function to generate sequence like "PPP", "YYY", "TTT", "HHH", "OOO", "NNN". 
You may cast it to the list for testing purposes. 
Write your code in `simple.py`.
### 2. 
In the `transposed_matrix.py` you can see the matrix you have to transpose: 
```
matrix = [[1, 2],
          [3, 4],
          [5, 6],
          [7, 8]]
```
Transpose it with generator expressions and get the result in `result_transposed` then test it with the 7th line of code. In the output you should see `[[1, 3, 5, 7], [2, 4, 6, 8]]`.
Additionally, transpose this matrix with `inner` and `outer` generator functions. To test it iterate by elements and print each element. Write your code in `result_transposed.py`. In the output, you should see
```
 1 
 3 
 5 
 7 
 2 
 4 
 6 
 8 
```