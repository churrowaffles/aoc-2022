with open('day10.txt', 'r') as file:
    instructions = [line.split() for line in file.readlines()]

value = 1
cycles = [1] # Value of Cycle 0 (before starting)

# With index representing the n-th cycle,
# record each cycle's value in a list
for instruct in instructions:
    if instruct[0] == 'noop':
        cycles.append(value)
    else:
        cycles += [value] * 2
        value += int(instruct[1])

# PART ONE
signal, cycle = 0, 20
while cycle <= 220:
    signal += cycle * cycles[cycle]
    cycle += 40

# PART ONE ANSWER
print(f"Signal Strength is {signal}")
# 14320


# PART TWO
image = []

# Skip cycles[0] as system officially starts at Cycle 1
for cycle, value in enumerate(cycles[1:]):
    if cycle % 40 in (value, value + 1, value - 1):
        image.append('#')
    else:
        image.append('.')

    if ((cycle+1) % 40) == 0:
        image.append('\n')

# PART TWO
print(''.join(image))

''' PART TWO ANSWER:
###...##..###..###..#..#..##..###....##.
#..#.#..#.#..#.#..#.#.#..#..#.#..#....#.
#..#.#....#..#.###..##...#..#.#..#....#.
###..#....###..#..#.#.#..####.###.....#.
#....#..#.#....#..#.#.#..#..#.#....#..#.
#.....##..#....###..#..#.#..#.#.....##..
'''