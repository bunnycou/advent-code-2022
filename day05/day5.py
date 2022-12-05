import copy

file = open("day5.txt")

lines = list()

for f in file.readlines():
    lines.append(f)
    
file.close()

# 0 through 8 are the stacks, 10 til the end are the instructions
# each stack is 4 chars wide "[x] " 9 stacks total

stacks = list()

# make a 2d list of the stacks
for stack in range(0,9):
    stacks.append(list()) # new list for stack
    for line in range(7,-1,-1):
        item = lines[line][(stack*4)+1]
        if item != " ":
            stacks[stack].append(item)

# duplicating stacks for part 2
stacks2 = copy.deepcopy(stacks)
#each line is 'move a from s to d', a can be double digit
for line in range(10, len(lines)):
    amnt = int(lines[line].split(" from")[0].split("move ")[1])
    srce = int(lines[line].split("from ")[1].split(" to")[0])-1
    dest = int(lines[line].split("to ")[1])-1
    
    for x in range(amnt):
        stacks[dest].append(stacks[srce].pop())
        
for x in range(0,9):
    print(stacks[x].pop(), end="")

print("\n") # seperator

# part 2
for line in range(10, len(lines)):
    amnt = int(lines[line].split(" from")[0].split("move ")[1])
    srce = int(lines[line].split("from ")[1].split(" to")[0])-1
    dest = int(lines[line].split("to ")[1])-1
    
    for x in range(amnt, 0, -1):
        stacks2[dest].append(stacks2[srce].pop(x*-1))

for x in range(0,9):
    print(stacks2[x].pop(), end="")