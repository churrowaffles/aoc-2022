def start_coordinate(text_file, heightmap):
    i, j, x, y = 0, 0, 0, 0

    with open(text_file) as file:
        for line in file.read():
            if line == 'S':
                x, y = i, j

            if line == '\n':
                j += 1
                i = 0
            else:
                heightmap[(i, j)] = line
                i += 1

    heightmap[(x, y)] = 'a'
    return (x,y)

def valid_coordinate(heightmap, current_c, compare_c):
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

def BFS(heightmap, distance, visited_locations, locations_to_visit):
    while locations_to_visit:
        location = locations_to_visit[0]

        if location is None:
            distance += 1
            locations_to_visit.append(None)

        elif not visited_locations.get(location):
            if heightmap[location] == 'E':
                return distance

            left = (location[0] - 1, location[1])
            right = (location[0] + 1, location[1])
            top = (location[0], location[1] - 1)
            bottom = (location[0], location[1] + 1)

            for c in [left, right, top, bottom]:
                if valid_coordinate(heightmap, location, c):
                    locations_to_visit.append(c)

            visited_locations[location] = distance

        locations_to_visit.pop(0)
        

# PART ONE SOLUTION
heightmap = {}
starting_point = start_coordinate('day12.txt', heightmap)
locations_to_visit = [starting_point, None]
shortest_path = BFS(heightmap, distance=0, visited_locations={}, locations_to_visit=locations_to_visit)
print(shortest_path)