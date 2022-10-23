# generator expressions
gen_ex = (letter * 3 for letter in "PYTHON")
gen_ex_2 = ("".join(letter) for letter in zip("PYTHON", "PYTHON", "PYTHON"))


# generator function
def gen_func(word: str = "PYTHON"):
    for three_letters in (letter * 3 for letter in word):
        yield three_letters
