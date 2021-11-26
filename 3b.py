import math
maximum = 0
for a in range(1,1001):
    for b in range(1,1001):
        if math.sqrt((a**2) + (b**2)) % 1 == 0:
            c = math.sqrt((a**2) + (b**2))
            if a*b*c > 1000000:
                break
            if a*b*c <= 1000000 and a*b*c > maximum:
                maximum = a*b*c
                print(a," ",b)
                print(maximum)
print(maximum)