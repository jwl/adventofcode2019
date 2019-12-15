import os

with open(
    os.path.join(os.getcwd(), "input.txt"),
    "r"
) as input_file:
    input = input_file.readlines()

# print(f"input is {input}")

sum = 0

for line in input:
    original_fuel = int(int(line) / 3) - 2
    fuel_total = original_fuel
    fuel = int(int(original_fuel) / 3) - 2
    while fuel > 0:
        fuel_total += fuel
        fuel = int(int(fuel) / 3) - 2

    print(f"line is {int(line)} and total fuel for this line is: {fuel_total}")
    sum += fuel_total

print(f"sum is: {sum}")
