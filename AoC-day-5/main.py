x = {"1": ["Z", "J", "N", "W", "P", "S"],
     "2": ["G", "S", "T"],
     "3": ["V", "Q", "R", "L", "H"],
     "4": ["V", "S", "T", "D"],
     "5": ["Q", "Z", "T", "D", "B", "M", "J"],
     "6": ["M", "W", "T", "J", "D", "C", "Z", "L"],
     "7": ["L", "P", "M", "W", "G", "T", "J"],
     "8": ["N", "G", "M", "T", "B", "F", "Q", "H"],
     "9": ["R", "D", "G", "C", "P", "B", "Q", "W"]
     }

y = x["6"]
print(y[-3:])

with open("data.txt") as file:
    data = file.readlines()
    for line in data:
        array = line.split()
        num_of_crates = int(array[1])
        get_stack = int(array[3])
        put_stack = int(array[5])
        a = x[f"{get_stack}"]
        b = x[f"{put_stack}"]
        b += a[-num_of_crates:]
        for _ in range(num_of_crates):
             a.pop()

        # for n in range(num_of_crates):
        #     a = x[f"{get_stack}"]
        #     b = x[f"{put_stack}"]
        #     b.append(a[-1])
        #     a.pop()
print(x)
