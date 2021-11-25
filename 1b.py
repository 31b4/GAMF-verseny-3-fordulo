with open('pi.txt') as f:
    line = f.readline()
odds=[]
odd=""
for num in line:
    if int(num)%2==1:
        odd+=num
    else:
        odds.append(odd)
        odd = ""
print(len(max(odds, key=len))) #lenght of the longest num
#print(max(odds, key=len)) #longest num