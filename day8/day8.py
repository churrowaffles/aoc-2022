def treeIsHidden(treemap, row, column, length):
    sides_blocked = 0
    current_tree_value = treemap[row][column]
    # Check left side
    for i in range(row):
        if current_tree_value <= treemap[i][column]:
            sides_blocked += 1
            break # if outer tree is blocking current tree
    # Check right side
    for i in range(length - row - 1):
        if current_tree_value <= treemap[row+i+1][column]:
            sides_blocked += 1
            break # if outer tree is blocking current tree
    # Check top
    for i in range(column):
        if current_tree_value <= treemap[row][i]:
            sides_blocked += 1
            break # if outer tree is blocking current tree
    # Check bottom
    for i in range(length - column - 1):
        if current_tree_value <= treemap[row][column+i+1]:
            sides_blocked += 1
            break # if outer tree is blocking current tree 
    
    if sides_blocked == 4:
        return 1
    else:
        return 0

def calculateScenicScore(treemap, row, column, length):
    left = right = top = bottom = 0

    # Check top
    move_row, move_column = row - 1, column
    while move_row > 0 and treemap[row][column] > treemap[move_row][column]:
        top += 1
        move_row -= 1
    top += 1

    # Check bottom
    move_row, move_column = row + 1, column
    while move_row < length - 1 and treemap[row][column] > treemap[move_row][column]:
        bottom += 1
        move_row += 1
    bottom += 1

    # Check left
    move_row, move_column = row, column - 1
    while move_column > 0 and treemap[row][column] > treemap[row][move_column]:
        left += 1
        move_column -= 1
    left += 1

    # Check right
    move_row, move_column = row, column + 1
    while move_column < length - 1 and treemap[row][column] > treemap[row][move_column]:
        right += 1
        move_column += 1
    right += 1
    
    return(top * bottom * left * right)


# Parse input into 2D Array
with open('day8.txt', 'r') as file:
    treemap = [line.rstrip() for line in file.readlines()]

length_of_side = len(treemap[0])

# PART 1
# Loop through all tree values that are not at the edge
hidden_trees = 0
row = column = 1
while row > 0 and row < length_of_side - 1:
    while column > 0 and column < length_of_side - 1:
        hidden_trees += treeIsHidden(treemap, row, column, length_of_side)
        column += 1
    row += 1
    column = 1

total_trees = length_of_side * length_of_side
visible_trees = total_trees - hidden_trees

print("Visible trees:", visible_trees)
# Visible trees: 1812

# PART 2
highest_scenic_score = 0
row = column = 1
# Loop through all tree values
while row > 0 and row < length_of_side - 1:
    while column > 0 and column < length_of_side - 1:
        scenic_score = calculateScenicScore(treemap, row, column, length_of_side)
        if highest_scenic_score < scenic_score:
            highest_scenic_score = scenic_score
        column += 1
    column = 1
    row += 1

print("Highest scenic score:", highest_scenic_score)
# Highest scenic score: 315495