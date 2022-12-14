def treeIsHidden(treemap, row, column):
    sides_blocked = 0
    current_tree_value = treemap[row][column]
    # Check top
    for r in treemap[:row][::-1]:
        if r[column] >= current_tree_value:
            sides_blocked += 1
            break

    # Check bottom
    for r in treemap[row+1:]:
        if r[column] >= current_tree_value:
            sides_blocked += 1
            break

    # Check left
    for col in treemap[row][:column][::-1]:
        if col >= current_tree_value:
            sides_blocked += 1
            break

    # Check right
    for col in treemap[row][column+1:]:
        if col >= current_tree_value:
            sides_blocked += 1
            break
    
    if sides_blocked == 4:
        return 1
    return 0


def calculateScenicScore(treemap, row, column):
    # Account for the last tree seen (or edge tree)
    left = right = top = bottom = 1
    current_tree_value = treemap[row][column]

    # Ignore all edge trees
    # Check top
    for r in treemap[1:row][::-1]:
        if r[column] >= current_tree_value:
            break
        top += 1

    # Check bottom
    for r in treemap[row+1:-1]:
        if r[column] >= current_tree_value:
            break
        bottom += 1

    # Check left
    for col in treemap[row][1:column][::-1]:
        if col >= current_tree_value:
            break
        left += 1

    # Check right
    for col in treemap[row][column+1:-1]:
        if col >= current_tree_value:
            break
        right += 1

    return(top * bottom * left * right)


# Parse input into 2D Array
with open('day8.txt', 'r') as file:
    treemap = [line.rstrip() for line in file.readlines()]

length_of_side = len(treemap[0])

# PART 1 & 2
row = column = 1

hidden_trees = 0
highest_scenic_score = 0

# Loop through all tree values that are not at the edge
while row > 0 and row < length_of_side - 1:
    while column > 0 and column < length_of_side - 1:

        # calculate how many trees are hidden
        hidden_trees += treeIsHidden(treemap, row, column)

        # calculate scenic score of each tree
        scenic_score = calculateScenicScore(treemap, row, column)
        if highest_scenic_score < scenic_score:
            highest_scenic_score = scenic_score
        
        column += 1
    row += 1
    column = 1


total_trees = length_of_side * length_of_side
visible_trees = total_trees - hidden_trees

print("Visible trees:", visible_trees)
# Visible trees: 1812

print("Highest scenic score:", highest_scenic_score)
# Highest scenic score: 315495