with open("day09/inputs/input-part2.in") as input_file:
    puzzle_input = input_file.read()


def is_valid(index, row_index):
    return 0 <= index < len(heightmap) and 0 <= row_index < len(heightmap[index])


heightmap = [list(map(int, line)) for line in puzzle_input.strip().split("\n")]

basin_sizes = []

for index in range(len(heightmap)):
    for row_index in range(len(heightmap[index])):
        queue = [(index, row_index)]
        basin = set()

        while queue:
            element = queue.pop(0)

            if is_valid(element[0] - 1, element[1]) and heightmap[element[0] - 1][element[1]] != 9 and heightmap[element[0] - 1][element[1]] > heightmap[element[0]][element[1]]:
                queue.append((element[0] - 1, element[1]))
            if is_valid(element[0], element[1] - 1) and heightmap[element[0]][element[1] - 1] != 9 and heightmap[element[0]][element[1] - 1] > heightmap[element[0]][element[1]]:
                queue.append((element[0], element[1] - 1))
            if is_valid(element[0], element[1] + 1) and heightmap[element[0]][element[1] + 1] != 9 and heightmap[element[0]][element[1] + 1] > heightmap[element[0]][element[1]]:
                queue.append((element[0], element[1] + 1))
            if is_valid(element[0] + 1, element[1]) and heightmap[element[0] + 1][element[1]] != 9 and heightmap[element[0] + 1][element[1]] > heightmap[element[0]][element[1]]:
                queue.append((element[0] + 1, element[1]))

            basin.add(element)

        basin_sizes.append(len(basin))

solution = 1
for basin_size in sorted(basin_sizes)[-3:]:
    solution *= basin_size

print(solution)
