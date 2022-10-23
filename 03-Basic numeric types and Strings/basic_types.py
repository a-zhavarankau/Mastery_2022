# 1. Slicing string

# Write slices to get the following strings.
# - `bcd`
# - `abcdefg`
# - `------`
# - `dcb`

string = "a0-b1-c2-d3-e4-f5-g6"

st1 = string[3:10:3]
st2 = string[::3]
st3 = string[2::3]
st4 = string[3:10][::-3]
result_1 = f"{st1}\n{st2}\n{st3}\n{st4}"
print(result_1)


# 2. Integer sum
integer_number_one = "125"
integer_number_two = "296"

int_1, int_2 = map(int, (integer_number_one, integer_number_two))
result_2 = str(int_1+int_2)
print(result_2)

# 3. Binary sum

binary_number_one = "0101"
binary_number_two = "11"
num_dec_1, num_dec_2 = map(lambda x: int(x, 2), (binary_number_one, binary_number_two))
summa = num_dec_1 + num_dec_2
result_3 = str(bin(summa)).lstrip("0b")
print(result_3)
