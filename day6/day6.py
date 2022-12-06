with open('day6.txt', 'r') as file:
    datastream = file.read()

def getStartOfMessage(distinct_characters):
    startmarker = endmarker = 0
    tracker = {}

    while endmarker < len(datastream):
        if tracker.get(datastream[endmarker]):
            startmarker = endmarker = tracker[datastream[endmarker]] + 1
            tracker.clear()
        tracker[datastream[endmarker]] = endmarker
        endmarker += 1

        if endmarker - startmarker == distinct_characters:
            return endmarker

# Part 1:
print(getStartOfMessage(4))

# Part 2:
print(getStartOfMessage(14))