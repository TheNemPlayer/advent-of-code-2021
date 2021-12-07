with open("day07/inputs/input-part1.in") as input_file:
    puzzle_input = input_file.read()

positions = list(map(int, puzzle_input.strip().split(",")))

best_fuel_cost = max(positions) * len(positions)

for attempt in range(max(positions) + 1):
    current_fuel_cost = 0

    for position in positions:
        current_fuel_cost += abs(position - attempt)

    best_fuel_cost = min(current_fuel_cost, best_fuel_cost)

print(best_fuel_cost)
