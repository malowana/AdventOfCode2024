import functions as f
import re

input_string = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

#Read the content of the file
file_path = "inputs\\day_4.txt"
input_string = f.read_txt(file_path)

# Split into a grid
grid = input_string.splitlines()
rows = len(grid)
cols = len(grid[0])

all_lines = []
count = 0
count2 = 0

# Horizontal lines (left-to-right)
all_lines.extend(grid)

# Vertical lines (top-to-bottom)
for col in range(cols):
    vertical = ''.join(grid[row][col] for row in range(rows))
    all_lines.append(vertical)

# Diagonals (down-right)
for row in range(rows):
    for col in range(cols):
        diagonal = ''.join(grid[row + i][col + i] for i in range(min(rows - row, cols - col)))
        if row == 0 or col == 0:
            all_lines.append(diagonal)

# Diagonals (up-right)
for row in range(rows):
    for col in range(cols):
        diagonal = ''.join(grid[row - i][col + i] for i in range(min(row + 1, cols - col)))
        if row == rows-1 or col == 0:
            all_lines.append(diagonal)

pattern = r"(?=(XMAS|SAMX))"

for line in all_lines:
    matches = [match.group(1) for match in re.finditer(pattern, line)]
    count += len(matches)

print(f"Part 1: {count}")

# part 2
for row in range(1, rows-1):
    for col in range(1, cols-1):
        if grid[row][col] == 'A':
            if (grid[row-1][col-1] == 'M' and grid[row+1][col+1] == 'S') or \
                    (grid[row-1][col-1] == 'S' and grid[row+1][col+1] == 'M'):
                if (grid[row - 1][col + 1] == 'M' and grid[row + 1][col - 1] == 'S') or (
                        grid[row - 1][col + 1] == 'S' and grid[row + 1][col - 1] == 'M'):
                    count2 += 1

print(f"Part 2: {count2}")