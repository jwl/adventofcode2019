import os

with open(
    # os.path.join(os.getcwd(), "test.txt")
    os.path.join(os.getcwd(), "input.txt")
    # os.path.join(os.getcwd(), "1202_alarm_input.txt")
) as input_file:
    input = input_file.read().rstrip().split(",")

input = [int(i) for i in input]

position = 0

print(f"input: {input}, length is: {len(input)}")

# for opcode in input:
    # print(f"at position {position}, opcode is: {opcode}")
    # position += 1
while position < len(input):
    print(f"at position {position}, opcode is: {input[position]}")

    if input[position] == 1:
        print(f"input1 value: {input[input[position+1]]}")
        print(f"input2 value: {input[input[position+2]]}")
        print(f"output to position: {input[input[position+3]]}")
        input[input[position+3]] = input[input[position+1]] + input[input[position+2]]
        position += 4
    elif input[position] == 2:
        input[input[position+3]] = input[input[position+1]] * input[input[position+2]]
        position += 4
    elif input[position] == 99:
        break
    else:
        print(f"something went wrong, halting program at position {position} on value {input[position]}!")
        break



print(f"at end of program, input is: {input}")

