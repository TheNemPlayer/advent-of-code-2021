with open("day06/inputs/input-part2.in") as input_file:
    puzzle_input = input_file.read()

lanternfish_list = list(map(int, puzzle_input.strip().split(",")))

lanternfish_days = [0 for _ in range(9)]

for lanternfish_day in lanternfish_list:
    lanternfish_days[lanternfish_day] += 1

for _ in range(256):
    new_lanternfish = lanternfish_days[0]

    for index in range(1, 9):
        lanternfish_days[index - 1] = lanternfish_days[index]

    lanternfish_days[6] += new_lanternfish
    lanternfish_days[8] = new_lanternfish

print(sum(lanternfish_days))
