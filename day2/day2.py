with (open('day2.txt', 'r')) as file:
    pairs = [lines.rstrip().replace(' ', '') for lines in file]

results = {'AX': 4, 'AY': 8, 'AZ': 3,
            'BX': 1, 'BY': 5, 'BZ': 9,
            'CX': 7, 'CY': 2, 'CZ': 6}

myscore = 0
for pair in pairs:
    myscore += results[pair]

print(myscore)
# 15691

# To decode what I will need to choose: Z = Win, X = Lose, Y = Draw
win_draw_lose = {
    'Z': {'A': 'Y', 'B': 'Z', 'C': 'X'},
    'X': {'A': 'Z', 'B': 'X', 'C': 'Y'},
    'Y': {'A': 'X', 'B': 'Y', 'C': 'Z'}
}

myscore = 0
for pair in pairs:
    pair = pair[0] + win_draw_lose[pair[1]][pair[0]]
    myscore += results[pair]

print(myscore)
# 12989