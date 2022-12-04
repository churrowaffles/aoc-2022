all_overlaps = 0


# PART ONE
with(open('day4.txt', 'r') as file):
    elvesvalue = [line.rstrip().replace('-', ',').split(',') for line in file]
    for value in elvesvalue:
        if value[0] == value[2] or value[1] == value[3]:
            all_overlaps += 1
        elif int(value[0]) > int(value[2]):
            if int(value[1]) < int(value[3]):
                all_overlaps += 1
        elif int(value[1]) > int(value[3]):
            all_overlaps += 1

print(all_overlaps)

# PART TWO
all_overlaps = 0

with(open('day4.txt', 'r') as file):
    allelves = [line.rstrip().split(',') for line in file]
    for eachpair in allelves:
        twoelves = [i.split('-') for i in eachpair]
        if twoelves[0][0] == twoelves[1][0] or twoelves[0][1] == twoelves[1][1] or twoelves[0][0] == twoelves[1][1] or twoelves[0][1] == twoelves[1][0]:
            all_overlaps += 1
        elif not(int(twoelves[0][1]) < int(twoelves[1][0]) or int(twoelves[1][1]) < int(twoelves[0][0])):
            all_overlaps += 1

print(all_overlaps)