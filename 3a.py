import math
counter = 0;
a = 15
for b in range(1,1000001):
    if math.sqrt((a**2) + (b**2)) % 1 == 0:
        counter+=1
        print(a," ",b)
print(counter)