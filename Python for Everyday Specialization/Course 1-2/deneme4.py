# Use the file name deneme_4.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
sum = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x = line.find("0")
    y = float(line[x:])
    sum = sum + y
    count = count + 1

print("Average spam confidence: ", (sum/count))
