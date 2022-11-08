from typing import Dict, List
import enum


class Instruction(enum.Enum):
    LOAD_VALUE = enum.auto()
    ADD_TWO_VALUES = enum.auto()
    PRINT_ANSWER = enum.auto()


class Interpreter:
    def __init__(self):
        self.stack: List[int] = []

    def LOAD_VALUE(self, number: int):
        self.stack.append(number)

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def ADD_TWO_VALUES(self):
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        total = first_num + second_num
        self.stack.append(total)

    def run_code(self, what_to_execute: Dict):
        instructions = what_to_execute["instructions"]
        numbers = what_to_execute["numbers"]

        for each_step in instructions:
            instruction, argument = each_step
            if instruction == Instruction.LOAD_VALUE:
                number = numbers[argument]
                self.LOAD_VALUE(number)
            elif instruction == Instruction.ADD_TWO_VALUES:
                self.ADD_TWO_VALUES()
            elif instruction == Instruction.PRINT_ANSWER:
                self.PRINT_ANSWER()
