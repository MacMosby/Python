def add(*args):
    total = 0
    for n in args:
        total += n
    return total


sum = add(3, 6, 1, 14, 27, 2)
print(sum)
