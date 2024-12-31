import re
import functions as f

input_string = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

# Read the content of the file
file_path = "inputs\\day_13.txt"
input_string = f.read_txt(file_path)

pattern = r"Button A: X[+=](\d+), Y[+=](\d+)\s+" \
          r"Button B: X[+=](\d+), Y[+=](\d+)\s+" \
          r"Prize: X[=](\d+), Y[=](\d+)"

results = []
total_list = []
for match in re.finditer(pattern, input_string):
    a_coords = [int(match.group(1)), int(match.group(2))]  # Button A
    b_coords = [int(match.group(3)), int(match.group(4))]  # Button B
    prize_coords = [int(match.group(5)), int(match.group(6))]  # Prize
    results.append({"Button A": a_coords, "Button B": b_coords, "Prize": prize_coords})

for idx, result in enumerate(results, start=1):
    buttonAX = result['Button A'][0]
    buttonAY = result['Button A'][1]
    buttonBX = result['Button B'][0]
    buttonBY = result['Button B'][1]
    prizeX = result['Prize'][0]
    prizeY = result['Prize'][1]

    bil = (buttonBX * buttonAY) - (buttonAX * buttonBY)
    b = ((prizeX * buttonAY) - (prizeY * buttonAX)) / bil
    a = (prizeY - (b * buttonBY)) / buttonAY

    if (isinstance(a, (int, float)) and a.is_integer()) and (isinstance(b, (int, float)) and b.is_integer()):
        total = a * 3 + b
        total_list.append(total)

sum_total = int(sum(total_list))
print(f"Part 1: {sum_total}")

# part 2
sum_total = []

for idx, result in enumerate(results, start=1):
    buttonAX = result['Button A'][0]
    buttonAY = result['Button A'][1]
    buttonBX = result['Button B'][0]
    buttonBY = result['Button B'][1]
    prizeX = result['Prize'][0] + 10000000000000
    prizeY = result['Prize'][1] + 10000000000000

    bil = (buttonBX * buttonAY) - (buttonAX * buttonBY)
    b = ((prizeX * buttonAY) - (prizeY * buttonAX)) / bil
    a = (prizeY - (b * buttonBY)) / buttonAY

    if (isinstance(a, (int, float)) and a.is_integer()) and (isinstance(b, (int, float)) and b.is_integer()):
        total = a * 3 + b
        total_list.append(total)

sum_total = int(sum(total_list))
print(f"Part 2: {sum_total}")
