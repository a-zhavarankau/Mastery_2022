# Files

## Exercises  

###1. 
The file `height.txt` has a table in TSV format with information about the height of students in the different classes of the school.
Write a program that reads this file and creates the file `output.txt` with the average student's height for each class.
The file consists of a set of lines, each with three fields:

    • Class
    • Surname
    • Height
The class is indicated only by a number. Letter modifiers are not used. The class number can be from 1 to 11 inclusive. There are no spaces in the surname, and a natural number is used as the height, but when calculating the average, you need to calculate the value in the floating form rounding to two decimal places.
Information on average height should be displayed in ascending order of the class number (for classes from one through eleven). If there is no information about a class, it is necessary to display a dash in front of it.
As a response, commit the file with the received data on average height. Write your code in `main.py`.

#### Example

```
1: 128,22
2: 132,91
3: 137,16
4: -
5: -
6: 156.04
7: 158.09
8: -
9: -
10: -
11: 172.74
```