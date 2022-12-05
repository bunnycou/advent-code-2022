file = open("day2.txt", "r")

# A is rock
# B is paper
# C is scissors
# X is rock
# Y is paper
# Z is scissors
# 0 for loss, 3 for tie, 6 for win
# 1 for rock, 2 for paper, 3 for scissors
score = 0
f = file.readlines()
file.close()

# part 1
for l in f:
    x = l.strip().split(" ")
    match x[0]:
        case "A":
            match x[1]:
                case "X":
                    score += 3+1
                case "Y":
                    score += 6+2
                case "Z":
                    score += 0+3
                case _:
                    print("A + x[1] didn't return a correct letter")
        case "B":
            match x[1]:
                case "X":
                    score += 0+1
                case "Y":
                    score += 3+2
                case "Z":
                    score += 6+3
                case _:
                    print("B + x[1] didn't return a correct letter")
        case "C":
            match x[1]:
                case "X":
                    score += 6+1
                case "Y":
                    score += 0+2
                case "Z":
                    score += 3+3
                case _:
                    print("C + x[1] didn't return a correct letter")
        case _:
            print("x[0] didn't return a correct letter")
    
print(score)

score = 0

# part 2
# A is rock
# B is paper
# C is scissors
# X means lose
# Y means draw
# Z means win
# 0 for loss, 3 for tie, 6 for win
# 1 for rock, 2 for paper, 3 for scissors
for l in f:
    x = l.strip().split(" ")
    match x[0]:
        case "A":
            match x[1]:
                case "X":
                    score += 0+3
                case "Y":
                    score += 3+1
                case "Z":
                    score += 6+2
                case _:
                    print("A + x[1] didn't return a correct letter")
        case "B":
            match x[1]:
                case "X":
                    score += 0+1
                case "Y":
                    score += 3+2
                case "Z":
                    score += 6+3
                case _:
                    print("B + x[1] didn't return a correct letter")
        case "C":
            match x[1]:
                case "X":
                    score += 0+2
                case "Y":
                    score += 3+3
                case "Z":
                    score += 6+1
                case _:
                    print("C + x[1] didn't return a correct letter")
        case _:
            print("x[0] didn't return a correct letter")
    
print(score)