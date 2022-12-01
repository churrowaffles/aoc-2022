with open('day1input.txt', 'r') as file:
    input = file.readlines()

this_elf_calories = 0
highest_calories = 0
elves = []

for line in input:
    if line == '\n':
        if this_elf_calories > highest_calories:
            highest_calories = this_elf_calories
        elves.append(this_elf_calories)
        this_elf_calories = 0
    else:
        this_elf_calories += int(line.strip())

print(f"Highest Calories is {highest_calories}")
# Highest Calories is 69501

elves.sort(reverse=True)
top_three = elves[0] + elves[1] + elves[2]
print(f"Top three is {top_three}")
# Top three is 202346