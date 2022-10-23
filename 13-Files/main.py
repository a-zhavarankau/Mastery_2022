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


# Iterate file row by row
def get_row_from_file(filename):
    with open(filename, encoding='utf-8') as file:
        for row in file.readlines():
            yield row


def create_classes() -> dict:
    classes = {}
    filename = 'height.txt'

    gen = get_row_from_file(filename)
    while True:
        try:
            row = next(gen)
        except StopIteration:
            break

        pupil = Pupil.get_pupil_from_row(row)
        class_num = pupil.class_num
        if class_num not in classes:
            classes[class_num] = Class(class_num)  # Create new class if class_num not in 'classes'
            classes[class_num].pupils.append(pupil)
        else:
            classes[class_num].pupils.append(pupil)
    return classes


if __name__ == '__main__':
    # Get all existing classes into dict 'classes'
    classes = create_classes()

    for class_num in range(1, 12):
        if class_num not in classes:
            classes[class_num] = Class(class_num)
            print(f'Class {class_num} average height is: -')
        else:
            class_avg_height = classes[class_num].get_avg_height()
            print(f'Class {class_num} average height is: {class_avg_height:.2F}')
