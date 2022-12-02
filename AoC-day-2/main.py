with open("data.txt") as file:
    data = file.readlines()
    print(data)

score = 0
for line in data:
    array = line.split()
    print(array)
    if array[0] == "A":
        if array[1] == "X":
            score += 3
        elif array[1] == "Y":
            score += 4
        else:
            score += 8
    elif array[0] == "B":
        if array[1] == "X":
            score += 1
        elif array[1] == "Y":
            score += 5
        else:
            score += 9
    elif array[0] == "C":
        if array[1] == "X":
            score += 2
        elif array[1] == "Y":
            score += 6
        else:
            score += 7
print(score)




