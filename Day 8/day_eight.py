import re

with open('input.txt', 'r') as file:
    data = file.read().splitlines()

# Putting data into a dictionary
inst_dict = {}
for line in enumerate(data):
    instructions = re.search("(\w{3})\s(\+|\-)(\d*)", line[1]).groups()
    operation = instructions[0]
    accumulate = int(f"{instructions[1]}{instructions[2]}")
    inst_dict[line[0]] = [operation, accumulate]


visited = []
visiting_key = 0
accumulator = 0

while visiting_key not in visited:
    visited.append(visiting_key)
    operation, accumulate = inst_dict[visiting_key]

    if operation == 'nop':
        visiting_key += 1
    if operation == "acc":
        accumulator += accumulate
        visiting_key += 1
    if operation == 'jmp':
        visiting_key += accumulate

print(f"Part One:\nAccumulator: {accumulator}\n")


# Part Two
visited = []
visiting_key = 0
accumulator = 0

while visiting_key in inst_dict:
    if visiting_key == 298:
        visiting_key += 1
    else:
        visited.append(visiting_key)
        operation, accumulate = inst_dict[visiting_key]
        if operation == 'nop':
            visiting_key += 1
        if operation == "acc":
            accumulator += accumulate
            visiting_key += 1
        if operation == 'jmp':
            visiting_key += accumulate

print(f"Part Two\nAccumulator: {accumulator}")
