import pandas

data1 = pandas.read_csv("file1.txt", names=["number"]).number
data2 = pandas.read_csv("file2.txt", names=["number"]).number

data_1 = [int(n) for n in data1]
data_2 = [int(n) for n in data2]

result = [item for item in data_1 if item in data_2]
print(result)


