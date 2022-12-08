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
score = 0

#need to go from tree and out, start would be tree position and end would be the edge (could be 0 or max size)
# after would need to go up and before would need to go down
def sceneScore(list, line, char):
    tree = int(list[line][char])
    total = 1

    taller = False
    start = line+1
    end = len(list)-1
    if start <= end:
        while not taller and start < end: # from tree down
            if int(list[start][char]) >= tree:
                taller = True
            else:
                start += 1
        total *= (start - line)
    else: total = 0

    taller = False
    start = char+1
    end = len(list[0])-1
    if start <= end:
        while not taller and start < end: # from tree to right
            if int(list[line][start]) >= tree:
                taller = True
            else:
                start += 1
        total *= (start - char)
    else: total = 0

    taller = False
    start = char-1
    end = 0
    if start >= end:
        while not taller and start > end: # from tree to left
            if int(list[line][start]) >= tree:
                taller = True
            else:
                start -= 1
        total *= (char - start)
    else: total = 0

    taller = False
    start = line-1
    end = 0
    if start >= end:
        while not taller and start > end: # from tree up
            if int(list[start][char]) >= tree:
                taller = True
            else:
                start -= 1
        total *= (line - start)
    else: total = 0
    
    return total

for l in range(listLength): # each line
    for c in range(lineLength): # each char in a line
        score = sceneScore(lines, l, c)
        if score > scenicScore:
            scenicScore = score
            scenicSpot = [l, c]
            
print(scenicScore)