fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "txtS/deneme_4.txt"

fh = open(fname)
count = 0
yep = list()

for line in fh:
    if line.startswith("From:"):
        continue
    elif line.startswith("From"):
        a = line.split()
        yep.append(a[1])

while count < len(yep): 
    print(yep[count])
    count += 1

print("There were", count, "lines in the file with From as the first word")