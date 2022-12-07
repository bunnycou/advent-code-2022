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
            t += total(newpath, t)
    print(t)
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
# size of /
totalSpace = 70000000
spaceNeeded = 30000000
spaceMax = totalSpace - spaceNeeded
totalSize = total("/", 0) # this number is way too big...

print(spaceMax, totalSize)

# looked at this guy for some inspiration https://github.com/tobstern/AoC2022/blob/master/day07.py