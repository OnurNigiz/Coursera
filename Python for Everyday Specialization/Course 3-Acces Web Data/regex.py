import re

name = input("Enter file:")
if len(name) < 1:
    name = "txtS/regex_sum_1584312.txt"
handle = open(name)

sumList = list()
sum = 0

for line in handle:
    i = re.findall('[0-9]+', line)
    if i == []:
        continue
    else:
        for k in i:
            k = int(k)
            sumList.append(k)

for number in sumList:
    sum = sum + number

print(sum)