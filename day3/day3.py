# PART ONE
def sumOfProperties(input):
    sum = 0
    # For each rucksack (line)
    with (open(input, 'r')) as file:
        for line in file:
            itemtype = itemType(line.rstrip())
            sum += convertToPriority(itemtype)
        return sum

def itemType(rucksack):
    letterExists = {}
    # Get the midpoint
    length = int(len(rucksack)/2)
    # Check the first half
    for letter in rucksack[:length]:
        letterExists[letter] = 1
    # Check the second half to see if letter existed in first half
    for letter in rucksack[length:]:
        if letterExists.get(letter):
            return letter

def convertToPriority(letter):
    if letter.isupper():
        return (ord(letter) - 38)
    return (ord(letter) - 96)

print(sumOfProperties('day3.txt'))
# 8185

# PART TWO
def sumOfProperties2(input):
    sum = i = 0
    # For each rucksack (line)
    with (open(input, 'r')) as file:
        group = []
        for line in file:
            i += 1
            group.append(line.rstrip())
            if i == 3:
                sum += convertToPriority(itemType2(group))
                i = 0
                group.clear()
    return sum
            
def itemType2(elves):
    letterExists = {}
    # Check the first guy
    for letter in elves[0]:
        letterExists[letter] = 1
    # Check the second guy
    for letter in elves[1]:
        if letterExists.get(letter) == 1:
            letterExists[letter] += 1
    # Check the third guy
    for letter in elves[2]:
        if letterExists.get(letter) == 2:
            return letter
    

print(sumOfProperties2('day3.txt'))
# 2817