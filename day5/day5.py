import re
from copy import deepcopy

# Read the input into a list
with open('day5.txt') as file:
    text = [line.rstrip() for line in file]

# Split the list into pattern and instructions
for index, contents in enumerate(text):
    if contents == '':
        pattern, instructions = text[:index], text[index+1:]
        break

# Create dictionaries for the stacks
stacks1 = {int(i): [] for i in pattern[-1].replace(' ', '')}

# Parse the stacks into a dict of lists
for layer in reversed(pattern[:-1]):
    stackposition = 1
    i = 1
    while stackposition < len(layer):
        if layer[stackposition] != ' ':
            stacks1[i].append(layer[stackposition])
        i += 1
        stackposition += 4

# Copy for part 2 solve
stacks2 = deepcopy(stacks1)

# Implement the instructions line by line
for line in instructions:
    number_of_stacks, move_from, move_to = list(map(int, (re.findall('\d+', line))))

    # Part 1 Solve
    for i in range(number_of_stacks):
        stacks1[move_to].append(stacks1[move_from].pop())

    # Part 2 Solve
    stacks2[move_to].extend(stacks2[move_from][-number_of_stacks:])
    del stacks2[move_from][-number_of_stacks:]


print(''.join([i[-1] for i in stacks1.values()]))
# Part 1: CNSZFDVLJ
print(''.join([i[-1] for i in stacks2.values()]))
# Part 2: QNDWLMGNS