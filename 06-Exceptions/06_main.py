import argparse
import sys
from itertools import zip_longest


class CustomAPIException(Exception):
    """ Class for customer exceptions"""


def get_pets():
    count = args.count

    # Check if file exists
    try:
        with open('file_db.txt', 'r') as f:
            pets_lines_raw = f.readlines()
    except FileNotFoundError:
        raise CustomAPIException("File not found")
    else:
        pets_lines = [line.strip("\n") for line in pets_lines_raw if line != "\n"]

    # Check if the file is empty (or was filled with newline characters)
    if len(pets_lines) == 0:
        raise CustomAPIException("File of pets is empty")

    if count > len(pets_lines):
        raise CustomAPIException("Not enough pets to show")

    data_keys = ["type", "name", "gender", "color"]
    pets = []
    for pet_line in pets_lines[:count]:
        pet_characteristics = pet_line.split()
        # Fill in the blank fields with the "N/A"
        pets.append(dict(zip_longest(data_keys, pet_characteristics, fillvalue='N/A')))
    return pets


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pet reader')
    parser.add_argument('count', type=int, help='number of pets')

    # Check if input character exists and if it is exactly one nonzero positive numeric
    try:
        assert len(sys.argv) == 2
        assert all((sys.argv[1].isdigit(), sys.argv[1] != "0"))
    except AssertionError:
        print("Wrong count of pets. Please enter one nonzero positive digit.")
        sys.exit()

    args = parser.parse_args()

    try:
        pets_data = get_pets()
    except CustomAPIException as ex:
        print(ex)
        sys.exit()

    print(pets_data)
