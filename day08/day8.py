file = open("day8.txt", "r")

lines = list()

for f in file.readlines():
    lines.append(f.strip())

file.close()

# part 1

def visible(start, end, list, line, char, ud, after):
    taller = False
    tree = int(list[line][char])
    if after:
        start += 1
    if ud:
        for a in range(start, end):
            if int(list[a][char]) >= tree:
                taller = True
    else:
        for a in range(start, end):
            if int(list[line][a]) >= tree:
                taller = True
    
    return not taller


total = 0
listLength = len(lines)
lineLength = len(lines[0])

for l in range(listLength): # each line
    for c in range(lineLength): # each character in a line
        if c == 0 or l == 0 or c == lineLength-1 or l == listLength-1:
            total += 1
        
        elif visible(0, c, lines, l, c, False, False) or visible(c, lineLength, lines, l, c, False, True) or visible(0, l, lines, l, c, True, False) or visible(l, listLength, lines, l, c, True, True):
            # compare from left, right, up, down
            total += 1
        
print(total)

#part 2

scenicScore = 0
scenicSpot = [0, 0]