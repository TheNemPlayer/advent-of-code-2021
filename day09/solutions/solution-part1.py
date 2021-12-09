with open("day09/inputs/input-part1.in") as input_file:
    puzzle_input = input_file.read()

heightmap = [list(map(int, line)) for line in puzzle_input.strip().split("\n")]

solution = 0

for index in range(len(heightmap)):
    for row_index in range(len(heightmap[index])):
        values = []

        try:
            values.append(heightmap[index][row_index - 1])
        except IndexError:
            pass

        try:
            values.append(heightmap[index][row_index + 1])
        except IndexError:
            pass

        try:
            values.append(heightmap[index - 1][row_index])
        except IndexError:
            pass

        try:
            values.append(heightmap[index + 1][row_index])
        except IndexError:
            pass

        if min(values) > heightmap[index][row_index]:
            solution += heightmap[index][row_index] + 1

print(solution)
