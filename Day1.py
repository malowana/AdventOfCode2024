import functions as f
from collections import Counter

# Input string in the given format
input_string = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

#Read the content of the file
file_path = "inputs\\day_1.txt"
input_string = f.read_txt(file_path)


list_final = []

# Split input string into lines and then into two separate lists
lines = input_string.split("\n")
list_left = sorted([int(line.split()[0]) for line in lines])
list_right = sorted([int(line.split()[1]) for line in lines])

#part1
for i in range(0, len(list_left)):
    difference = abs(list_left[i]-list_right[i])
    list_final.append(difference)

output1 = sum(list_final)
print(f"Part 1: {output1}")

#part2
similarity_list = []
count_values = Counter(list_right)

for i in range(0, len(list_left)):
    new_value = list_left[i] * count_values[list_left[i]]
    similarity_list.append(new_value)

output2 = sum(similarity_list)
print(f"Part 2: {output2}")

