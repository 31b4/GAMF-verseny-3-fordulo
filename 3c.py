import math
counter = 0
for a in range(1,2400):
    for b in range(1,2400):
        if math.sqrt((a**2) + (b**2)) % 1 == 0:
            c = math.sqrt((a**2) + (b**2))
            if a+b+c == 2400:
                counter+=0.5
print(counter)