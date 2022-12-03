file = open("day3.txt", "r")

lines = list()

for f in file.readlines():
    lines.append(f.strip())
    
file.close()

#part 1
#ord(char)-64 gives value for A, ord(char)-96 gives value for a
# A is 1 and a is 1 for these, we need A to be 27
total = 0

for l in lines:
    l1 = l[0:int(len(l)/2)]
    l2 = l[int(len(l)/2):]

    for a in l1:
        if l2.find(a) != -1:
            if a.isupper():
                total += (ord(a)-64+26)
            if a.islower():
                total += (ord(a)-96)
            break
        
print(total)

#part 2
#compare 3 lines and find the common item then add up
total = 0

for i in range(0, len(lines)-1, 3):
    for a in lines[i]:
        if lines[i+1].find(a) != -1 and lines[i+2].find(a) != -1:
            if a.isupper():
                total += (ord(a)-64+26)
            if a.islower():
                total += (ord(a)-96)
            break

print(total)