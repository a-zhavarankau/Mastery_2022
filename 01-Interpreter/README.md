# Interpreter

This task will get you up and running with Python interpreter. 

## Exercises

### 1. Setup virtual environment  

Start by making sure that you have Python version 3.7+ installed.
Create isolated virtual environment. Using the links in the material for this module create virtual environment in the folder `.env` and activate it.

## 2. Simple python interpreter

In the `interpreter.py` file we implemented a simple interpreter that runs Python bytecode. In the `main.py` file we have a simple program that is stored in the `instructions` variable. What it does is:
- Loads value by index 0 from the `numbers` array into the stack
- Loads value by index 1 from the `numbers` array into the stack
- Pops those two values and adds them. The result is placed back into the stack
- Pops the last value from the stack and prints it into the console

If we run this program right now by calling `python main.py` we will get `7` printed in the console.
Your task is to modify the `main.py` file in such a way that all the values in the `numbers` array got added and print the result. In the end, when you run this program `12` should be printed in the console.
