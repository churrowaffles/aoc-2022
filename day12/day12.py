def start_and_end(text_file):
    i, j = 0, 0

    with open(text_file) as file:
        for line in file.read():
            if line == 'S':
                x, y = i, j

            if line == 'E':
                x2, y2 = i, j

            if line == '\n':
                j += 1
                i = 0
            else:
                heightmap[(i, j)] = line
                i += 1

    heightmap[(x, y)] = 'a'
    return ((x,y),(x2,y2))


def valid_coordinate(current_c, compare_c):
    if not heightmap.get(compare_c):
        return False
    
    if heightmap[compare_c] == 'E':
        compare = ord('z')
    else:
        compare = ord(heightmap[compare_c])

    current = ord(heightmap[current_c])

    if compare < current + 2:
        return True
    return False


def valid_coordinate_reverse(current_c, compare_c):
    if not heightmap.get(compare_c):
        return False
    
    current = ord(heightmap[current_c])
    compare = ord(heightmap[compare_c])

    if compare > current - 2:
        return True
    return False


def BFS(locations_to_visit, f, endpoint):
    distance = 0
    visited_locations = {}
    while locations_to_visit:
        location = locations_to_visit[0]

        if location is None:
            distance += 1
            locations_to_visit.append(None)

        elif not visited_locations.get(location):
            left = (location[0] - 1, location[1])
            right = (location[0] + 1, location[1])
            top = (location[0], location[1] - 1)
            bottom = (location[0], location[1] + 1)

            for c in [left, right, top, bottom]:
                if f(location, c):
                    if heightmap[c] == endpoint:
                        return distance + 1
                    locations_to_visit.append(c)

            visited_locations[location] = distance
        locations_to_visit.pop(0)
        

heightmap = {}
start_end_coordinates = start_and_end('day12.txt')
starting_point, ending_point = start_end_coordinates[0], start_end_coordinates[1]

# PART ONE SOLUTION
# Start from the starting point and navigate to 'E'
locations_to_visit = [starting_point, None]
shortest_path = BFS(locations_to_visit=locations_to_visit, f=valid_coordinate, endpoint='E')
print("Part One: The shortest path will take", shortest_path, "steps.")

# PART TWO SOLUTION
# Start from the 'E' and navigate to the nearest 'a'
locations_to_visit = [ending_point, None]
shortest_path = BFS(locations_to_visit=locations_to_visit, f=valid_coordinate_reverse, endpoint='a')
print("Part Two: The shortest path will take", shortest_path, "steps.")