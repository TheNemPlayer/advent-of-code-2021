with open("day08/inputs/input-part1.in") as input_file:
    puzzle_input = input_file.read()


def format_line(line):
    line = line.split(" | ")
    return line[0].split(" "), line[1].split(" ")


display = [format_line(line) for line in puzzle_input.strip().split("\n")]

count = 0

for digits in display:
    for digit in digits[1]:
        if len(digit) in [2, 3, 4, 7]:
            count += 1

print(count)
