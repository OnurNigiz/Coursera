largest = None
smallest = None
nbs = []

while True:
    num = (input("Enter a number: "))
    if num == "done":
        print("Invalid input")
        break
    try:
        num = float(num) 
    except:
        pass
    if type(num) == float:
        nbs.append(num)

largest_so_far = -1
smallest_so_far = None
for i in nbs:
    if i > largest_so_far:
        largest_so_far = i
largest = int(largest_so_far)   

for k in nbs:
    if smallest_so_far is None:
        smallest_so_far = k
    elif k < smallest_so_far:
        smallest_so_far = k
smallest = int(smallest_so_far )

print("Maximum is", largest)
print("Minimum is", smallest)