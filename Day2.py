import functions as f

# Input string in the given format
input_string = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

# Read the content of the file
file_path = "inputs\\day_2.txt"
input_string = f.read_txt(file_path)

lines = input_string.split("\n")

is_safe = 0
count_values = 0
incorrect_lists = []

for row in lines:
    current_list = [int(x) for x in row.split()]
    count_values = 0
    list_diff = []
    for value in range(1, len(current_list)):
        diff = current_list[value] - current_list[value - 1]
        list_diff.append(diff)
        if diff > 3 or diff < -3 or diff == 0:
            break
        else:
            count_values += 1
    same_chars = len(set(x > 0 for x in list_diff)) == 1
    if count_values == len(current_list) - 1 and same_chars == 1:
        is_safe = is_safe + 1
    else:
        incorrect_lists.append(current_list)

print(f"Part 1: {is_safe}")

# part2
count_values = 0

for incorrect_list in incorrect_lists:
    is_corrected = 0
    for i in range(0, len(incorrect_list)):
        if not is_corrected:
            new_list = incorrect_list.copy()
            del new_list[i]
            count_values = 0
            list_diff = []
            for value in range(1, len(new_list)):
                diff = new_list[value] - new_list[value - 1]
                list_diff.append(diff)
                if diff > 3 or diff < -3 or diff == 0:
                    break
                else:
                    count_values += 1

            same_chars = len(set(x > 0 for x in list_diff)) == 1
            if count_values == len(new_list) - 1 and same_chars == 1:
                is_safe = is_safe + 1
                is_corrected = 1

print(f"Part 2: {is_safe}")
