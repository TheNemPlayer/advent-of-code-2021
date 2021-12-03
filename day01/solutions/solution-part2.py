with open("day01/inputs/input-part2.in") as input_file:
    puzzle_input = input_file.read()

depths = list(map(int, puzzle_input.strip().split("\n")))
depth_sums = [sum(depth_window)
              for depth_window in zip(depths[:-2], depths[1:-1], depths[2:])]

previous_depth_sum = depth_sums[0]
increase_amount = 0

for depth_sum in depth_sums[1:]:
    if depth_sum > previous_depth_sum:
        increase_amount += 1
    previous_depth_sum = depth_sum

print(increase_amount)
