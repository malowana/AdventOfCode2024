import re
import functions as f

input_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

#Read the content of the file
file_path = "inputs\\day_3.txt"
input_string = f.read_txt(file_path)

mul_pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"  # mul(x,y)
accepted = re.findall(fr"{mul_pattern}", input_string)

total_sum = 0

for pair in accepted:
    number1, number2 = map(int, pair[0:2])
    total_sum += number1 * number2
print(f"Part 1: {total_sum}")

# part2
# input_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

do_pattern = r"(don't\(\)|do\(\))"  # "don't()" or "do()"
accepted = re.findall(fr"{do_pattern}|{mul_pattern}", input_string)

is_do = True  # Initial state
total_sum = 0
for item in accepted:
    if item[0] == "don't()":
        is_do = False
    elif item[0] == "do()":
        is_do = True
    elif item[1]:
        if is_do:
            number1, number2 = map(int, item[1:3])
            total_sum += number1 * number2

print(f"Part 2: {total_sum}")

