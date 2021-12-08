# Let's pretend I never wrote this code

with open("day08/inputs/input-part2.in") as input_file:
    puzzle_input = input_file.read()


import itertools


def format_line(line):
    line = line.split(" | ")
    return line[0].split(" "), line[1].split(" ")


display = [format_line(line) for line in puzzle_input.strip().split("\n")]

value = 0

for digits in display:
    for attempt in itertools.permutations(["a", "b", "c", "d", "e", "f", "g"]):
        values = set()
        for trial in digits[0]:
            if set(trial) == {attempt[2], attempt[5]}:
                values.add(1)
            elif set(trial) == {attempt[0], attempt[2], attempt[5]}:
                values.add(7)
            elif set(trial) == {attempt[1], attempt[2], attempt[3], attempt[5]}:
                values.add(4)
            elif set(trial) == set(attempt):
                values.add(8)
            elif set(trial) == {attempt[0], attempt[2], attempt[3], attempt[4], attempt[6]}:
                values.add(2)
            elif set(trial) == {attempt[0], attempt[1], attempt[3], attempt[5], attempt[6]}:
                values.add(5)
            elif set(trial) == {attempt[0], attempt[2], attempt[3], attempt[5], attempt[6]}:
                values.add(3)
            elif set(trial) == {attempt[0], attempt[1], attempt[2], attempt[4], attempt[5], attempt[6]}:
                values.add(0)
            elif set(trial) == {attempt[0], attempt[1], attempt[3], attempt[4], attempt[5], attempt[6]}:
                values.add(6)
            elif set(trial) == {attempt[0], attempt[1], attempt[2], attempt[3], attempt[5], attempt[6]}:
                values.add(9)
        if len(values) == 10:
            num = []
            for number in digits[1]:
                if set(number) == {attempt[2], attempt[5]}:
                    num.append("1")
                elif set(number) == {attempt[0], attempt[2], attempt[5]}:
                    num.append("7")
                elif set(number) == {attempt[1], attempt[2], attempt[3], attempt[5]}:
                    num.append("4")
                elif set(number) == set(attempt):
                    num.append("8")
                elif set(number) == {attempt[0], attempt[2], attempt[3], attempt[4], attempt[6]}:
                    num.append("2")
                elif set(number) == {attempt[0], attempt[1], attempt[3], attempt[5], attempt[6]}:
                    num.append("5")
                elif set(number) == {attempt[0], attempt[2], attempt[3], attempt[5], attempt[6]}:
                    num.append("3")
                elif set(number) == {attempt[0], attempt[1], attempt[2], attempt[4], attempt[5], attempt[6]}:
                    num.append("0")
                elif set(number) == {attempt[0], attempt[1], attempt[3], attempt[4], attempt[5], attempt[6]}:
                    num.append("6")
                elif set(number) == {attempt[0], attempt[1], attempt[2], attempt[3], attempt[5], attempt[6]}:
                    num.append("9")

            value += int("".join(num))
            break

print(value)
