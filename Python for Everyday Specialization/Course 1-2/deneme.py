hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter money per hour: ")
r = float(rate)


def computepay(hour, rate):
    if h <= 40:
        p = hour * rate
    else:
        p = ((hour-40) * rate * 1.5) + (40 * rate)
    
    return p

p = computepay(h, r)

print("Pay", p)