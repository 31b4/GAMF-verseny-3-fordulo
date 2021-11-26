with open('pi.txt') as f:
    line = f.readline()
max = 0

def isprime(num):
    print(num)
    for n in range(2,int(num**(1/2))+1):   
        if (num % n) == 0:  
            return False
    return True

for i in range(len(line)):
    test = ""
    for j in range(i,i+11):
        if j == len(line):
            break
        test+=line[j]
        if isprime(int(test)) and int(test) >max:
            max = int(test)
print(max)