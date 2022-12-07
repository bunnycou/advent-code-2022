from collections import defaultdict

file = open("day7.txt", "r")

lines = list()

for f in file.readlines():
    lines.append(f.strip())
    
file.close()

dirs = defaultdict(list)
path = ""

for l in lines:

    if l.startswith("$"): # its a command

        if l.split(" ")[1] == "cd": # cd command
            dirname = l.split(" ")[2]

            if dirname == "..": # if we go up a directory
                path = "/".join(path.split("/")[:-1])
                if path == "":
                    path = "/"

            else: # if we have a directory to enter
                if dirname == "/":
                    path = "/"
                elif path == "/":
                    path = f"/{dirname}"
                else:
                    path = f"{path}/{dirname}"



    else: # its an entry

        if l.startswith("dir"): # directory entry
            dirname = l.split(" ")[1]
            dirs[path] += [dirname]

        else: # file entry
            fname = l.split(" ")[1]
            fsize = int(l.split(" ")[0])
            dirs[path] += [fsize]

# go through each directory and find total size, size needs to be below or equal to 100000, add the size to total
#need a recursive function
# this works but it doesn't work
def total(path, t):
    for x in dirs[path]:
        if type(x) == int: # when x is a file size
            t += x
        else: # when x is a directory
            if path == "/":
                newpath = f"/{x}"
            else:
                newpath = f"{path}/{x}"
            t += total(newpath, 0)
    return t

result = 0
for k in dirs:
    amount = total(k, 0)
    if amount <= 100000:
        result += amount

print(result)

#part 2

# drive space 70000000
# free space needed 30000000
totalSpace = 70000000
spaceNeeded = 30000000
spaceMax = totalSpace - spaceNeeded
totalSize = total("/", 0) # size of /
deleteSize = totalSize - spaceMax

delDirs = list()
# find dir closest to delete size
for k in dirs:
    amount = total(k, 0)
    if amount >= deleteSize:
        delDirs.append(amount) # if I needed the folder name I could add K and make this a dictionary, I don't so I won't complicate this further

# sort the list by ascending and print lowest value
sorted = 0
while sorted != -1:
    for x in range(len(delDirs)-1):
        if delDirs[x] > delDirs[x+1]:
            sorted = 1
            delDirs[x], delDirs[x+1] = delDirs[x+1], delDirs[x]
    if sorted == 0:
        sorted = -1
    else:
        sorted = 0

print(delDirs[0])

# looked at this guy for some inspiration https://github.com/tobstern/AoC2022/blob/master/day07.py