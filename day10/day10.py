file = open("day10.txt", "r")

lines = list()

for f in file.readlines():
    lines.append(f.strip())
    
file.close()

cycle = [1]

for l in lines:
    if l.startswith("addx"):
        val = int(l.split(" ")[1])
        cycle.append(cycle[-1])
        cycle.append(cycle[-1]+val)
    else:
        cycle.append(cycle[-1])
     
cycle20 = cycle[20-1]
cycle20str = cycle20*20
cycle60 = cycle[60-1]
cycle60str = cycle60*60
cycle100 = cycle[100-1]
cycle100str = cycle100*100
cycle140 = cycle[140-1]
cycle140str = cycle140*140
cycle180 = cycle[180-1]
cycle180str = cycle180*180
cycle220 = cycle[220-1]
cycle220str = cycle220*220

total = cycle20str + cycle60str + cycle100str + cycle140str + cycle180str + cycle220str
print(len(cycle), total)

# part2
crt = list()
sprStr = 0
sprEnd = 2
curpos = 0

def draw():
    global curpos, sprStr, sprEnd, crt
    if curpos%40 == 0:
        crt.append("")
    if curpos%40 in range(sprStr, sprEnd):
        crt[int(curpos/40)] += "#"
    else:
        crt[int(curpos/40)] += "." 
    curpos+=1

for l in lines:
    if l.startswith("addx"):
        val = int(l.split(" ")[1])
        draw()
        draw()
        sprStr += val
        sprEnd += val
    else:
        draw()
       

for c in crt:
    print(c)