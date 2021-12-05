with open("day05/inputs/input-part2.in") as input_file:
    puzzle_input = input_file.read()


def vent_range(start, end):
    x1, y1 = map(int, start.split(","))
    x2, y2 = map(int, end.split(","))

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            yield x1, y
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            yield x, y1
    else:
        if x1 < x2:
            if y1 < y2:
                for x, y in zip(range(x1, x2 + 1), range(y1, y2 + 1)):
                    yield x, y
            else:
                for x, y in zip(range(x1, x2 + 1), range(y1, y2 - 1, -1)):
                    yield x, y
        else:
            if y1 < y2:
                for x, y in zip(range(x1, x2 - 1, -1), range(y1, y2 + 1)):
                    yield x, y
            else:
                for x, y in zip(range(x1, x2 - 1, -1), range(y1, y2 - 1, -1)):
                    yield x, y


vents = puzzle_input.strip().split("\n")

vents_list = [
    pair for vent in vents for pair in vent_range(*vent.split(" -> "))]

vents_set = set()
vent_repeats = set()

for vent in vents_list:
    if vent in vents_set:
        vent_repeats.add(vent)
    else:
        vents_set.add(vent)

print(len(vent_repeats))
