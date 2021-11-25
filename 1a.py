with open('pi.txt') as f:
    line = f.readline()
nums = [0,1,2,3,4,5,6,7,8,9]
counters = [0,0,0,0,0,0,0,0,0,0]
for num in line:
    counters[nums.index(int(num))] +=1
print(nums[counters.index(max(counters))]) #most used num