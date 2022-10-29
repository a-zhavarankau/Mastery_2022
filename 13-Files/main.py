class Pupil:
    def __init__(self, class_num: int, surname: str, height: int):
        self.class_num = class_num
        self.surname = surname
        self.height = height

    @staticmethod
    def get_pupil_from_row(row):
        class_num, surname, height = map(lambda x: int(x) if x.isdigit() else x, row.split())
        pupil = Pupil(class_num, surname, height)
        return pupil


class Class:
    def __init__(self, class_num: int | str):
        self.class_num = class_num
        self.pupils = []

    def get_avg_height(self) -> float:
        pupils_amount = len(self.pupils)
        sum_height = sum((pupil.height for pupil in self.pupils))
        return sum_height / pupils_amount

    def get_class_info(self):
        if self.pupils:
            avg_height = f'{self.get_avg_height():.2F}'
        else:
            avg_height = '-'
        return f'Class {self.class_num} average height is: {avg_height}'


def get_row_from_file(filename):
    # Iterate file row by row
    with open(filename, encoding='utf-8') as file:
        for row in file.readlines():
            yield row


def create_classes_from_file(filename) -> dict:
    # Create classes that mentioned in the file
    classes = {}

    gen = get_row_from_file(filename)
    while True:                          # Get rows one-by-one
        try:
            row = next(gen)
        except StopIteration:
            break

        pupil = Pupil.get_pupil_from_row(row)
        class_num = pupil.class_num
        if class_num not in classes:
            classes[class_num] = Class(class_num)  # Create new class if class_num not in 'classes'
        classes[class_num].pupils.append(pupil)
    return classes


def create_classes(filename) -> dict:
    # Create all classes from 1 to 11
    existing_classes = create_classes_from_file(filename)
    for class_num in range(1, 12):
        if not existing_classes.get(class_num):  # Check if class not exists
            existing_classes[class_num] = Class(class_num)  # Create new empty class
    return existing_classes


def print_classes(filename):
    classes = create_classes(filename)
    for class_num in range(1, 12):
        print(classes[class_num].get_class_info())


if __name__ == '__main__':
    print_classes('height.txt')