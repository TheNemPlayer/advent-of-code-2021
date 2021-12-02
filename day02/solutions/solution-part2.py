with open("day02/inputs/input-part2.in") as input_file:
    puzzle_input = input_file.read()

def format_command(command):
    instruction, value = command.split()
    return instruction, int(value)

commands = list(map(format_command, puzzle_input.strip().split("\n")))

aim = 0
horizontal_position = 0
depth = 0

for command in commands:
    if command[0] == "forward":
        horizontal_position += command[1]
        depth += aim * command[1]
    elif command[0] == "down":
        aim += command[1]
    else:
        aim -= command[1]

print(horizontal_position * depth)
