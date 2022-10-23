classes = {i: [] for i in range(1, 12)}

with open("height.txt", encoding='utf-8') as file:
    for line in file:
        cl, _, height = line.strip("\n").split("\t")
        classes[int(cl)].append(int(height))


def avg_height(arr):
    if arr == []:
        return "-"
    return f"{sum(arr) / len(arr):.2f}"


for i in classes:
    print(f"{i}: {avg_height(classes[i])}")

# Create another file containing necessary information
with open("avg_heights.txt", "w", encoding='utf-8') as file:
    for i in classes:
        file.write(f"{i}: {avg_height(classes[i])}\n")
