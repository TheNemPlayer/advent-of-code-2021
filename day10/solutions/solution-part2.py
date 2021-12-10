with open("day10/inputs/input-part2.in") as input_file:
    puzzle_input = input_file.read()

closing = {"(": ")", "[": "]", "{": "}", "<": ">"}
points = {")": 1, "]": 2, "}": 3, ">": 4}

lines = puzzle_input.strip().split("\n")

solutions = []

for line in lines:
    queue = []

    for character in line:
        if character in ("(", "[", "{", "<"):
            queue.append(character)
        elif closing[queue[-1]] == character:
            del queue[-1]
        else:
            queue = None
            break

    try:
        score = 0
        for bracket in queue[::-1]:
            score *= 5
            score += points[closing[bracket]]
        solutions.append(score)
    except TypeError:
        pass

print(sorted(solutions)[len(solutions) // 2])
