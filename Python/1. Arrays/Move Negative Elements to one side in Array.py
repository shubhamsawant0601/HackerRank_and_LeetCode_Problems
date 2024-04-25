# Move Negative Elements to one side in Array

a = [-1,2,45,7,33,5,-2,-4,55,-5,-56,-4,-3,23,-34]

index = 0
for i in range(len(a)):
    if a[i]<0:
        a[index],a[i] = a[i], a[index]
        index+=1
        
print(a)