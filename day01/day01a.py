#!/usr/bin/python3

f = open("input01.txt", "r")
col1 = []
col2 = []

for line in f:
    nums = line.strip().split()
    col1.append(int(nums[0]))
    col2.append(int(nums[1]))

col1.sort()
col2.sort()

sum = 0
for i in range(len(col1)):
    sum += abs(col1[i] - col2[i])

print(sum)

f.close()