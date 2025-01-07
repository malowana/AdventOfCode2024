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


# count2 = 0
# for line in all_lines:
#     pattern = r"(?=(MAS|SAM))"
#
#     # Szukanie wszystkich dopasowań (uwzględniając nakładanie)
#     matches = [match.group(1) for match in re.finditer(pattern, line)]
#     c = len(matches)
#     count2 += c
# print(count2)
# Wzorce do dopasowania
# patterns = [r"M.S", r"\.A\.", r"M.S"]
#
# # Liczenie dopasowań dla każdego wzorca
# total_matches = 0
# for pattern in patterns:
#     matches = re.findall(pattern, input_string, flags=re.DOTALL)  # DOTALL uwzględnia wielowierszowość
#     total_matches += len(matches)
#     print(f"Wzorzec '{pattern}': {len(matches)} dopasowań")
#
# # Wyświetlanie całkowitej liczby dopasowań
# print(f"Łączna liczba dopasowań: {total_matches}")

# lines = input_string.split('\n')
# data = [list(line) for line in lines]
#
# # Create a DataFrame
# df = pd.DataFrame(data)
#
#
#
# def find_xmas(df):
#     rows, cols = df.shape
#     target = "XMAS"
#     target2 = "SAMX"
#     result = []
#
#     # Check horizontally
#     for i in range(rows):
#         row_str = ''.join(df.iloc[i, :])
#         #print(row_str)
#         if target in row_str:
#             print(row_str)
#             result.append((f"Row {i+1}", "Horizontal", row_str.index(target)))
#             print((f"{target} Row {i+1}", "Horizontal", row_str.index(target)))
#         if target2 in row_str:
#             result.append((f"Row {i+1}", "Horizontal2", row_str.index(target2)))
#             print(row_str)
#             print((f"{target2} Row {i + 1}", "Horizontal2", row_str.index(target2)))
#
#     #
#     #print("Check vertically")
#     for j in range(cols):
#         col_str = ''.join(df.iloc[:, j])
#         #print(col_str)
#         if target in col_str:
#             print(col_str)
#             result.append((f"Column {j+1}", "Vertical", col_str.index(target)))
#             print((f"Column {j+1}", "Vertical", col_str.index(target)))
#         if target2 in col_str:
#             print(col_str)
#             result.append((f"Column {j+1}", "Vertical2", col_str.index(target2)))
#             print((f"Column {j + 1}", "Vertical", col_str.index(target2)))
#
#
#     # Check diagonally (top-left to bottom-right)
#     # for k in range(-rows + 1, cols):  # Diagonal indices
#     #     df[0][0]
#     #     df[0][1]+
#
#         # diag_str = ''.join(df.iloc[h, h - k] for h in range(max(0, k), min(rows, cols + k)) if 0 <= h - k < cols)
#         # print(diag_str)
#         # if target in diag_str:
#         #     print(diag_str)
#         #     result.append((f"Diagonal starting at ({max(0, k)+1}, {max(0, -k)+1})", "Diagonal TL-BR", diag_str.index(target)))
#         #     print((f"Diagonal starting at ({max(0, k)+1}, {max(0, -k)+1})", "Diagonal TL-BR", diag_str.index(target)))
#         # if target2 in diag_str:
#         #     print(diag_str)
#         #     result.append((f"Diagonal2 starting at ({max(0, k)+1}, {max(0, -k)+1})", "Diagonal TL-BR", diag_str.index(target2)))
#         #     print((f"Diagonal starting at ({max(0, k) + 1}, {max(0, -k) + 1})", "Diagonal TL-BR", diag_str.index(target2)))
#
#     # # Check diagonally (top-right to bottom-left)
#     # for k in range(-rows + 1, cols):
#     #     diag_str2 = ''.join(df.iloc[i, k + i] for i in range(max(0, -k), min(rows, cols - k)) if 0 <= k + i < cols)
#     #     print(diag_str2)
#     #     if target in diag_str2:
#     #         print(diag_str2)
#     #         result.append((f"trDiagonal starting at ({max(0, -k)+1}, {cols - min(rows, cols - k)})", "Diagonal TR-BL", diag_str2.index(target)))
#     #         print((f"trDiagonal starting at ({max(0, -k)+1}, {cols - min(rows, cols - k)})", "Diagonal TR-BL", diag_str2.index(target)))
#     #     if target2 in diag_str2:
#     #         print(diag_str2)
#     #         result.append((f"trDiagonal2 starting at ({max(0, -k)+1}, {cols - min(rows, cols - k)})", "Diagonal TR-BL", diag_str2.index(target2)))
#     #         print((f"trDiagonal starting at ({max(0, -k) + 1}, {cols - min(rows, cols - k)})", "Diagonal TR-BL",
#     #                diag_str2.index(target2)))
#     #
#     #     # Check diagonally (bottom-right to top-left)
#     #     for k in range(-rows + 1, cols):
#     #         diag_str3 = ''.join(
#     #             df.iloc[rows - 1 - i, cols - 1 - (i - k)] for i in range(max(0, k), min(rows, cols + k)) if
#     #             0 <= cols - 1 - (i - k) < cols)
#     #         if target in diag_str3:
#     #             start_row = rows - 1 - (max(0, k) + diag_str3.index(target))
#     #             start_col = cols - 1 - (diag_str3.index(target) + max(0, -k))
#     #             result.append((f"Diagonal BR-TL starting at ({start_row + 1}, {start_col + 1})", "Diagonal",
#     #                            diag_str3.index(target)))
#     #         if target2 in diag_str3:
#     #             start_row = rows - 1 - (max(0, k) + diag_str3.index(target2))
#     #             start_col = cols - 1 - (diag_str3.index(target2) + max(0, -k))
#     #             result.append((f"Diagonal BR-TL (Reversed) starting at ({start_row + 1}, {start_col + 1})", "Diagonal",
#     #                            diag_str3.index(target2)))
#
#     return result
#
# # Find XMAS
# xmas_locations = find_xmas(df)
#
# # # Print results
# # for location in xmas_locations:
# #     print(f"Found 'XMAS' at: {location}")
#
# print(len(xmas_locations))
# #1244 - too low
