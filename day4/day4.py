file = open("day4.txt", "r")

lines = list()

for f in file.readlines():
    lines.append(f.strip())
    
file.close()

total = 0

#part 1
for x in lines:
    pair = x.split(",")
    first = pair[0].split("-")
    second = pair[1].split("-")
    
    # python was comparing numbers as strings
    first[0], first[1] = int(first[0]), int(first[1])
    second[0], second[1] = int(second[0]), int(second[1])
    
    if (first[0] >= second[0] and first[1] <= second[1]) or (second[0] >= first[0] and second[1] <= first[1]):
        total += 1
        
print(total)

total = 0

#part 2, any overlap
for x in lines:
    pair = x.split(",")
    first = pair[0].split("-")
    second = pair[1].split("-")
    
    # python was comparing numbers as strings
    first[0], first[1] = int(first[0]), int(first[1])
    second[0], second[1] = int(second[0]), int(second[1])
    
    if ((first[0] >= second[0] and first[0] <= second[1]) or (first[1] >= second[0] and first[1] <= second[1])) or ((second[0] >= first[0] and second[0] <= first[1]) or (second[1] >= first[0] and second[1] <= first[0])):
        total += 1

print(total)