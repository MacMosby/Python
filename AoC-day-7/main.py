with open("data.txt") as file:
    data = file.readlines()

print(data)

tree = {

}

for n in range(len(data)):
    item = data[n].strip()

    if item == "$ ls":
        directory = ((data[n-1]).split())[2]
        print(directory)



print("/")