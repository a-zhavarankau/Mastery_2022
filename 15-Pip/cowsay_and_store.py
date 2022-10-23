from cowsay import get_output_string

with open("cowsay.txt", "w") as file:
    result = get_output_string("cow", "Hello world")
    file.write(result)
