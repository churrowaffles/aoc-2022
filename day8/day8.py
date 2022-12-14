# Parse input into 2D Array
with open('day8.txt', 'r') as file:
    treemap = [line.rstrip() for line in file.readlines()]

length_of_side = len(treemap[0])

hidden_trees = 0
highest_scenic_score = 0

# Loop through all tree values that are not at the edge
row = column = 1
while row > 0 and row < length_of_side - 1:
    while column > 0 and column < length_of_side - 1:

        sides_blocked = 0
        left = right = top = bottom = 0
        current_tree_value = treemap[row][column]

        # Check top
        for r in treemap[:row][::-1]:
            top += 1
            if r[column] >= current_tree_value:
                sides_blocked += 1
                break

        # Check bottom
        for r in treemap[row+1:]:
            bottom += 1
            if r[column] >= current_tree_value:
                sides_blocked += 1
                break

        # Check left
        for col in treemap[row][:column][::-1]:
            left += 1
            if col >= current_tree_value:
                sides_blocked += 1
                break

        # Check right
        for col in treemap[row][column+1:]:
            right += 1
            if col >= current_tree_value:
                sides_blocked += 1
                break
        
        if sides_blocked == 4:
            hidden_trees += 1

        # Calculate scenic score of this tree
        scenic_score = top * bottom * left * right
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