"""
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.

Example
a = [1,1,2,2,4,4,5,5,5]

There are two subarrays meeting the criterion:[1,1,2,2]  and [4,4,5,5,5]. The maximum length subarray has 5 elements.
"""


def pickingNumbers(a):
    li = []
    a.sort()
    for i in range(len(a)):
        for j in range(i, len(a)):

            set_ = set(a[i:j])

            arr = list(set_)

            if len(set_) == 2:
                if abs(arr[0]-arr[1])==1:
                    li.append(a[i:j])
                
    
    li.sort(key = lambda x: len(x), reverse=True)

    return(len(li[0]))

""" -------------------------------------or------------------------------------- """

def pickingNumbers(a):
    max = 0
    dic = dict(Counter(a))
    dic = dict(sorted(dic.items(), key=lambda x:x[0]))
    keys = list(dic.keys())
    
    for i in range(len(keys)-1):
        
        if keys[i+1]-keys[i]==1:
            count = dic[keys[i+1]]+dic[keys[i]]
        
            if count>max:
                max = count
    
    return max
              


                