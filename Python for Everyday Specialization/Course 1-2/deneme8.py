name = input("Enter file:")
if len(name) < 1:
    name = "deneme_4.txt"
handle = open(name)

times = list()
count = dict()

for line in handle:
    if line.startswith("From:"):
        continue
    elif line.startswith("From"):
        a = line.split()
        b = a[5].split(":")
        times.append(b[0])

for time in times:
    count[time] = count.get(time, 0) + 1

srt_count = list()

for k,v in count.items():
    new = (k,v)
    srt_count.append(new)

srt_count = sorted(srt_count)

for k,v in srt_count[:len(srt_count)]:
    print(k,v)