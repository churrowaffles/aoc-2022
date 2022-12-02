with (open('day2.txt', 'r')) as file:
    txt = [lines.rstrip() for lines in file]
    print(txt)
    lines = file.read().replace(' ', '').replace('X', 'A').replace('Y', 'B').replace('Z', 'C')
    

results = {'A A': [4, 4], 'A B': [1, 7], 'A C': [7, 1],
            'B A': [7, 1], 'B B': [4, 4], 'B C': [1, 7],
            'C A': [1, 7], 'C B': [7, 1], 'C C': [4, 4]}
