def move(rope, direction):
    if direction == 'R':
        rope[0] += 1
    elif direction == 'L':
        rope[0] -= 1
    elif direction == 'U':
        rope[1] += 1
    elif direction == 'D':
        rope[1] -= 1

def no_move(head, tail):
    # Same Row
    if head[0] == tail[0]:
        # Same Column OR 1 Column away
        if head[1] == tail[1] or abs(tail[1] - head[1]) == 1:
            return True
    # Same Column
    elif head[1] == tail[1]:
        # 1 Row away
        if abs(tail[0] - head[0]) == 1:
            return True
    # Diagonally connected (1 Column and 1 Row away)
    elif abs(tail[0] - head[0]) == 1 and abs(tail[1] - head[1]) == 1:
        return True

def move_tail(head, tail):
    if not no_move(head, tail):
        # if they are in the same row or column,
        # move tail 1 time in the same direction
        x_distance = head[0] - tail[0]
        y_distance = head[1] - tail[1]

        if x_distance == 0:
            tail[1] += y_distance // 2
        elif y_distance == 0:
            tail[0] += x_distance // 2
        else:
        # if they are diagonally apart 2 blocks away,
        # move in the direction diagonally
            if abs(x_distance) == abs(y_distance) == 2:
                tail[0] += x_distance // 2
                tail[1] += y_distance // 2
            elif abs(x_distance) == 2:
                tail[0] += x_distance // 2
                tail[1] += y_distance
            elif abs(y_distance) == 2:
                tail[0] += x_distance
                tail[1] += y_distance // 2

with open('day9.txt', 'r') as file:
    instructions = [line.rstrip().split() for line in file.readlines()]

# Instantiate head and tail
# (x, y) coordinates
head_p1 = [0, 0]
tail_p1 = [0, 0]
body_p2 = [[0, 0] for i in range(10)]

# Hash Table to represent visited coordinates 
# recorded in tuples e.g. (3, 5) or (0, -4)
visited_locations_p1 = {}
visited_locations_p1[(0, 0)] = True

visited_locations_p2 = {}
visited_locations_p2[(0, 0)] = True

for instruct in instructions:
    for i in range(int(instruct[1])):
        move(head_p1, instruct[0])
        move_tail(head_p1, tail_p1)
        visited_locations_p1[(tuple(tail_p1))] = True

        # Move the Head
        move(body_p2[0], instruct[0])
        index = 0
        while len(body_p2) - 1 > index:
            move_tail(body_p2[index], body_p2[index+1])
            index += 1
        visited_locations_p2[tuple(body_p2[-1])] = True
        
        '''
        # VISUALISATION: This visualisation will be upside down #
        # You may swap += and -= in 'U' and 'D' of move function to see it right side up #

        visualisation = [['.'] * 50 for i in range(50)]
        for i in body_p2:
            visualisation[15 + i[1]][15 + i[0]] = str(body_p2.index(i))
            if body_p2.index(i) == 0:
                visualisation[15 + i[1]][15 + i[0]] = 'h'
        visualisation[15][15] = 's'


        visual = [''.join(v) for v in visualisation]
        for i in visual:
            print(i)
        '''

# Part One
print(f'Visited Locations: {len(visited_locations_p1)}')
# Visited Locations: 6098

# Part Two
print(f'Visited Locations: {len(visited_locations_p2)}')
# Visited Locations: 2597