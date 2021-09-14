"""
A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, 
find the cost to buy them. If it is not possible to buy both items, return -1.

Example
b = 60
keyboards = [40,50,60]
drives = [5,8,12]


The person can buy a 40 keyboard+12 USB = 52 , or a 50 keyboard + 8 USB = 58. Choose the latter as the more expensive option and return 58 .
"""

def getMoneySpent(keyboards, drives, b):
    li = []
    max = 0
    for i in keyboards:
        for j in drives:
            if sum([i,j])<=b:
                li.append([i,j])
    
    for i in li:
        if sum(i) > max:
            max = sum(i)
    
    if len(li)==0:
        return -1
        
    return max