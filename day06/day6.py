file = open("day6.txt", "r")

# today's input is one line
line = file.readline()

file.close()

buffer = ""
marker = 0

#part 1
for x in range(0, len(line)):
    char = line[x]
    if len(buffer) > 3:
        buffer = f"{buffer[1:]}{char}"
        for y in range(0,4):
            for z in range(y+1,4):
                if buffer[y] == buffer[z]:
                    marker += 1
        if marker > 0:
            marker = 0
        else:
            marker = x+1
            break
    else:
        buffer = f"{buffer}{char}"

print(marker)

buffer = ""
marker = 0

#part 2, same thing but 14 chars

for x in range(0, len(line)):
    char = line[x]
    if len(buffer) > 13:
        buffer = f"{buffer[1:]}{char}"
        for y in range(0,14):
            for z in range(y+1,14):
                if buffer[y] == buffer[z]:
                    marker += 1
        if marker > 0:
            marker = 0
        else:
            marker = x+1
            break
    else:
        buffer = f"{buffer}{char}"

print(marker)