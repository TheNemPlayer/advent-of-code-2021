with open("day06/inputs/input-part1.in") as input_file:
    puzzle_input = input_file.read()

lanternfish = list(map(int, puzzle_input.strip().split(",")))

for _ in range(80):
    new_lanternfish = 0
    for index in range(len(lanternfish)):
        if lanternfish[index] == 0:
            lanternfish[index] = 6
            new_lanternfish += 1
        else:
            lanternfish[index] -= 1

    lanternfish.extend([8 for _ in range(new_lanternfish)])

print(len(lanternfish))
