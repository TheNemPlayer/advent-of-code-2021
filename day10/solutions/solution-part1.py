with open("day10/inputs/input-part1.in") as input_file:
    puzzle_input = input_file.read()

closing = {"(": ")", "[": "]", "{": "}", "<": ">"}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}

lines = puzzle_input.strip().split("\n")

solution = 0

for line in lines:
    queue = []

    for character in line:
        if character in ("(", "[", "{", "<"):
            queue.append(character)
        elif closing[queue[-1]] == character:
            del queue[-1]
        else:
            solution += points[character]
            break

print(solution)
