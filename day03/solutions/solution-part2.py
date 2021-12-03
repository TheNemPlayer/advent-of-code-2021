with open("day03/inputs/input-part2.in") as input_file:
    puzzle_input = input_file.read()


def format_binary_number(binary_number):
    return list(map(int, list(binary_number)))


def list_to_decimal_number(a_list):
    decimal_number = 0

    for digit in a_list:
        decimal_number *= 2
        decimal_number += digit

    return decimal_number


binary_numbers = list(
    map(format_binary_number, puzzle_input.strip().split("\n")))

oxygen_generator_rating = []
co2_scrubber_rating = []

for index in range(len(binary_numbers[0])):
    oxygen_digit_frequency = 0
    oxygen_digit_amount = 0

    co2_digit_frequency = 0
    co2_digit_amount = 0

    for binary_number in binary_numbers:
        if binary_number[:index] == oxygen_generator_rating:
            oxygen_digit_frequency += binary_number[index]
            oxygen_digit_amount += 1
        if binary_number[:index] == co2_scrubber_rating:
            co2_digit_frequency += binary_number[index]
            co2_digit_amount += 1

    oxygen_generator_rating.append(
        oxygen_digit_frequency // ((oxygen_digit_amount + 1) // 2))

    if co2_digit_frequency == co2_digit_amount:
        co2_scrubber_rating.append(True)
    else:
        co2_scrubber_rating.append(
            not (co2_digit_frequency // ((co2_digit_amount + 1) // 2)))

oxygen_generator_rating = list_to_decimal_number(oxygen_generator_rating)
co2_scrubber_rating = list_to_decimal_number(co2_scrubber_rating)

print(oxygen_generator_rating * co2_scrubber_rating)
