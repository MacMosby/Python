priorities = ["0",
              "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
              "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


with open("data.txt") as file:
    data = file.readlines()

print(data)

sum_of_priorities = 0
num_of_line = len(data)
num_of_groups = int(num_of_line/3)


for n in range(num_of_groups):
    group = data[(0 + 3*n):(3 + 3*n)]
    print(group)

    items_list = group[0].strip()

    for letter in items_list:
        if letter in group[1] and letter in group[2]:
            print(letter)
            sum_of_priorities += priorities.index(letter)
            break



# for line in data:
#     items_list = line.strip()
#     num_of_items = len(items_list)
#     half = int(num_of_items/2)
#     print(half)
#     first_part = items_list[:half]
#     second_part = items_list[half:]
#     print(first_part)
#     print(second_part)
#
#     for letter in first_part:
#         if letter in second_part:
#             sum_of_priorities += priorities.index(letter)
#             print(letter)
#             break
print(sum_of_priorities)
