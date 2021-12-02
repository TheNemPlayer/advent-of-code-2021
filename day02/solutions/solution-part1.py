with open("day02/inputs/input-part1.in") as input_file:
    puzzle_input = input_file.read()

def format_command(command):
    instruction, value = command.split()
    return instruction, int(value)

commands = list(map(format_command, puzzle_input.strip().split("\n")))

horizontal_position = 0
depth = 0

for command in commands:
    if command[0] == "forward":
        horizontal_position += command[1]
    elif command[0] == "down":
        depth += command[1]
    else:
        depth -= command[1]

print(horizontal_position * depth)
