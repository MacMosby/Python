with open("data.txt") as file:
    data = file.readlines()

nums_of_cals = []
high_score = 0
actual_score = 0
for n in data:
    try:
        cals = int(n)
        actual_score += cals
    except ValueError:
        if actual_score > high_score:
            high_score = actual_score
        nums_of_cals.append(actual_score)
        actual_score = 0
nums_of_cals.append(actual_score)
nums_of_cals.sort(reverse=True)
print(high_score)
print(nums_of_cals[:3])
list_of_top_three = nums_of_cals[:3]

sum_of_top_three = 0
for n in list_of_top_three:
    sum_of_top_three += n

print(sum_of_top_three)



