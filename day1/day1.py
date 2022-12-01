f = open("day1.txt", "r")
l = list()
y = 0

# creates list of total calories per elf
for x in f.readlines():
    if x == "\n":
        l.append(y)
        y = 0
    else:
        y += int(x)
    
# l.sort(reverse=True)
# using built in sort kinda cheating
# using a bubble sort
unsorted = True
z = 0
while unsorted:
    for x in range(0, len(l)-1):
        y = x + 1
        if l[x] < l[y]:
            z += 1
            l[x], l[y] = l[y], l[x]
    if z == 0:
        unsorted = False
    else:
        z = 0

y = l[0] + l[1] + l[2]

# part 1 answer, part 2 answer
print(l[0], y)