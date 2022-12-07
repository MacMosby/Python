with open("data.txt") as file:
    buffer = file.read()
    print(buffer)

count = 0

for n in range(len(buffer) - 13):
    sequence = buffer[0 + n:14 + n]

    array = list(sequence)
    x = sorted(array)

    for m in range(13):
        if x[m] == x[m+1]:
            count = 0
            break
        else:
            count += 1
            if count == 13:
                print(sequence)
                print(n+14)
                break

