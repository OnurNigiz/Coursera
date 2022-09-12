name = input("Enter file:")
if len(name) < 1:
    name = "deneme_4.txt"
handle = open(name)

storage = dict()
yep = list()

for line in handle:
    if line.startswith("From:"):
        continue
    elif line.startswith("From"):
        a = line.split()
        yep.append(a[1])

for sender in yep:
    counts = yep.count(sender)
    storage[sender] = counts

mostSender = None
senderCounter = None
for sender,counts in storage.items(): 
    if senderCounter is None or counts > senderCounter :
        mostSender = sender
        senderCounter = counts


print(mostSender, senderCounter)