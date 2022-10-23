condition = True
count = 0

while True:
    if condition:
        count += 1
        condition = 12 - count
    else:
        break

print(count)
