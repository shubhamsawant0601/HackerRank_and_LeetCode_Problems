# Find Union and Intesection of two Arrays

a = [1,2,3,4,5,6,7,8]
b = [6,7,8,9,10,11,12]

intersection = []
union = []

# method to find Intesection
def find_intersection(a,b):
    intesection = []
    for i in a:
        if i in b:
            intersection.append(i)
            
    return intersection
      
# method to find Union
def find_union(a,b):
    union  = []
    for i in a:
        if i not in b:
            union.append(i)
    
    return union+b
    
print(find_intersection(a,b))
print(find_union(a,b))