with open("day01/inputs/input-part1.in") as input_file:
    puzzle_input = input_file.read()

depths = list(map(int, puzzle_input.strip().split("\n")))

previous_depth = depths[0]
increase_amount = 0

for depth in depths[1:]:
    if depth > previous_depth:
        increase_amount += 1
    previous_depth = depth

print(increase_amount)
