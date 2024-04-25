# Sort 0, 1 and 2 from array without using sorting algorithms

a = [1,0,2,1]

zero_count = 0
one_count = 0
two_count = 0

for i in a:
    if i == 0:
        zero_count+=1
    elif i == 1:
        one_count+=1
    elif i == 2:
        two_count+=1
    
li = []

for i in range(zero_count):
    li.append(0)
for i in range(one_count):
    li.append(1)
for i in range(two_count):
    li.append(2)

print(li)
