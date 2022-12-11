file = open("day9.txt", "r")

lines = list()

for f in file.readlines():
    lines.append(f.strip())

head = [0,0]
tail = [0,0]
spots = []

def move(direc, head, tail):
    match direc:
        case "U":
            head[1] += 1
            if tail[1] < head[1]-1:
                tail[1] += 1
                if tail[0] != head[0]:
                    tail[0] = head[0]
                    
        case "D":
            head[1] -= 1
            if tail[1] > head[1]+1:
                tail[1] -= 1
                if tail[0] != head[0]:
                    tail[0] = head[0]

        case "L":
            head[0] -= 1
            if tail[0] > head[0]+1:
                tail[0] -=1
                if tail[1] != head[1]:
                    tail[1] = head[1]

        case "R":
            head[0] += 1
            if tail[0] < head[0]-1:
                tail[0] += 1
                if tail[1] != head[1]:
                    tail[1] = head[1]
        

for l in lines:
    l = l.split(" ")
    direc = l[0]
    dist = int(l[1])
    
    for x in range(dist):
        move(direc, head, tail)
        if tail not in spots:
            spots.append(tail[:])

print(len(spots))

# part 2

spots.clear()

# reset head and tail
head = [0,0]
tail = [0,0]

# knot 1-9
k1 = [0,0]
k2 = [0,0]
k3 = [0,0]
k4 = [0,0]
k5 = [0,0]
k6 = [0,0]
k7 = [0,0]
k8 = [0,0]
k9 = [0,0]
                    
def update(head, tail):
    if tail[1] < head[1]-1: #if tail needs to move up
        tail[1] += 1
        if tail[0] != head[0]:
            tail[0] = head[0]
    
    if tail[1] > head[1]+1: # if tail needs to mvoe down
        tail[1] -= 1
        if tail[0] != head[0]:
            tail[0] = head[0]
    
    if tail[0] > head[0]+1: # if tail needs to move left
        tail[0] -= 1
        if tail[1] != head[1]:
            tail[1] = head[1]
    
    if tail[0] < head[0]-1: # if tail needs to move right               
        tail[0] += 1
        if tail[1] != head[1]:
            tail[1] = head[1]

for l in lines:
    l = l.split(" ")
    direc = l[0]
    dist = int(l[1])
    
    for x in range(dist):
        move(direc, head, k1)
        update(k1, k2)
        update(k2, k3)
        update(k3, k4)
        update(k4, k5)
        update(k5, k6)
        update(k6, k7)
        update(k7, k8)
        update(k8, k9)
        
        if k9 not in spots:
            spots.append(k9[:])
        
print(len(spots))