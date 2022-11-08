from interpreter import Interpreter

numbers = [3, 4, 5]
interpreter = Interpreter()

while len(numbers) > 1:
    interpreter.LOAD_VALUE(numbers[0])
    interpreter.LOAD_VALUE(numbers[1])
    interpreter.ADD_TWO_VALUES()
    del numbers[:2]
    numbers.insert(0, interpreter.stack[-1])
    del interpreter.stack[:-1]   # limit infinite stack growth

interpreter.PRINT_ANSWER()