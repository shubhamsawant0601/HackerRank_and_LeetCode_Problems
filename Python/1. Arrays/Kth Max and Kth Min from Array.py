# Kth Max and Kth Min from Array
a = [1,2,3,4,5,6,7,8,9,10]

# function kth max 
def k_max(a, n):
    a.sort()
    return a[-n]

# function kth min 
def k_min(a, n):
    a.sort()
    return a[n-1]

print(k_max(a,2))
print(k_min(a,2))
    