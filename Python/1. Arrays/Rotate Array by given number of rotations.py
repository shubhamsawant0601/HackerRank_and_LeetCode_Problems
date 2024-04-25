# Rotate Array by given number of rotations

a = [1,2,3,4,5,6,7,8,9,10]

def rotate(a, side):
    first = a[0]
    last = a[len(a)-1]
    
    # For Left Rotate
    if side=='L':
        for i in range(len(a)-1):
            a[i] = a[i+1]
        
        a[len(a)-1] = first
        
    # For Right Rotate
    if side=='R':
        for i in range(len(a)-1, 0, -1):
            a[i] = a[i-1]
            
        a[0] = last
       
    # Return List
    return a
        
    
    
for i in "LLRLRLRLRR":
    print(rotate(a, i))
    
# Output