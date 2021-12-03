with open("day03/inputs/input-part1.in") as input_file:
    puzzle_input = input_file.read()


def format_binary_number(binary_number):
    return list(map(int, list(binary_number)))


binary_numbers = list(
    map(format_binary_number, puzzle_input.strip().split("\n")))

digit_frequencies = list(map(sum, zip(*binary_numbers)))

gamma_rate = 0
epsilon_rate = 0

for digit_frequency in digit_frequencies:
    most_common_digit = digit_frequency > len(binary_numbers) // 2

    gamma_rate *= 2
    epsilon_rate *= 2

    gamma_rate += most_common_digit
    epsilon_rate += not most_common_digit

print(gamma_rate * epsilon_rate)
