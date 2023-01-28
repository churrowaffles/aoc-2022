from collections import defaultdict

class directory:
    def __init__(self, parent, name):
        self.name = name # Current node name (e.g. "/")
        self.parent = parent # Pointer to parent
        self.contents = {} # To hold the contents of the current directory


# Recursively calculate directory sizes 
def calculateDirectorySize(ptr, memo):
    if len(ptr.contents) == 0:
        return 0
        
    for key, value in ptr.contents.items():
        if isinstance(value, directory):
            memo[ptr.name] += calculateDirectorySize(value, memo)
        elif isinstance(value, str):
            memo[ptr.name] += int(value)
            
    return memo[ptr.name]


# For Part Two
def smallestDirectoryToDelete(directories):
    for i in sorted(directories.values()):
        if i > (30000000 - (70000000 - directories['/'])):
            return i


# Create the root directory
root = directory(parent=None, name="/")

# Read list of commands and parse input into root directory
with open('day7.txt', 'r') as file:
    for line in file:
        if not line == '$ ls\n':
            line = line.rstrip()
            if line == '$ cd /':
                ptr = root
            elif line == '$ cd ..':
                ptr = ptr.parent
            elif line.startswith('$ cd'):
                ptr = ptr.contents[line[5:]]
            else:
                if line.startswith('dir'):
                    newname = ptr.name + line[4:] + "/"
                    if not newname in ptr.contents:
                        newDir = directory(parent=ptr, name=newname)
                        ptr.contents[line[4:]] = newDir
                else:
                    line = line.split()
                    ptr.contents[line[1]] = line[0]

# Record size of each directory
directories = defaultdict(int)
calculateDirectorySize(root, directories)

# Part 1: Sum of directories with values <= 100000
print(sum([value for value in directories.values() if value <= 100000]))
# 1307902

# Part 2:
print(smallestDirectoryToDelete(directories))
# 7068748