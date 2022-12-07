file = open("day7.txt", "r")

lines = list()

for f in file.readlines():
    lines.append(f.strip())
    
file.close()

# considering using a default dictionary to create the tree structure...
# looking at this guy for some inspiration https://github.com/tobstern/AoC2022/blob/master/day07.py