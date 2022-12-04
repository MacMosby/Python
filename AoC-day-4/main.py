with open("data.txt") as file:
    data = file.readlines()

print(data)
count = 0

for line in data:
    pair = line.strip()
    split_pair = pair.split(",")
    print(split_pair)
    first = split_pair[0]
    second = split_pair[1]
    first_couple = first.split("-")
    second_couple = second.split("-")
    print(first_couple)
    print(second_couple)
    a = int(first_couple[0])
    b = int(first_couple[1])
    x = int(second_couple[0])
    y = int(second_couple[1])
    print(a)
    print(b)
    print(x)
    print(y)
    # if a < x:
    #     if b >= y:
    #         count += 1
    # elif x < a:
    #     if y >= b:
    #         count += 1
    # else:
    #     count += 1
    # print(count)
    if b < x:
        pass
    elif y < a:
        pass
    else:
        count += 1
print(count)

