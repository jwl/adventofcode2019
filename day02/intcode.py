"""intcode for Day2 of Advent of Code 2019."""

import os


def compute_intcode(noun: int, verb: int) -> int:
    """
    Computes output for intcode inputs.

    Args:
        noun: input 1, to be inserted at position 1
        verb: input 2, to be inserted at position 2
    
    Returns:
        Value at position 0.
    """
    with open(
        os.path.join(os.getcwd(), "starting_memory.txt")
    ) as starting_memory_file:
        memory_as_strings = starting_memory_file.read().rstrip().split(",")

    memory = [int(i) for i in memory_as_strings]
    memory[1] = noun
    memory[2] = verb

    instruction_pointer = 0

    while instruction_pointer < len(memory):
        if memory[instruction_pointer] == 1:
            memory[memory[instruction_pointer + 3]] = (
                memory[memory[instruction_pointer + 1]]
                + memory[memory[instruction_pointer + 2]]
            )
            instruction_pointer += 4
        elif memory[instruction_pointer] == 2:
            memory[memory[instruction_pointer + 3]] = (
                memory[memory[instruction_pointer + 1]]
                * memory[memory[instruction_pointer + 2]]
            )
            instruction_pointer += 4
        elif memory[instruction_pointer] == 99:
            break
        else:
            print(
                f"something went wrong, halting program at position {instruction_pointer} on value {memory[instruction_pointer]}!"
            )
            break

    return memory[0]


print(f"for inputs 1 and 1, compute_intcode(1,1) is: {compute_intcode(12,2)}")

inner_loop_broken = False

for noun in range(100):
    for verb in range(100):
        if compute_intcode(noun, verb) == 19690720:
            print(
                f"answer found! noun is {noun} and verb is {verb}. 100 * noun + verb is: {100 * noun + verb}"
            )
            inner_loop_broken = True
            break
    if inner_loop_broken:
        break

if not inner_loop_broken:
    print(f"answer not found!")
