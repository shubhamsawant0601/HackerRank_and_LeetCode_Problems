"""
Example

Password = "2bbbb"
This password is 5 characters long and is missing an uppercase and a special character. The minimum number of characters to add is 2.

Password = "2bb#A"
This password is 5 characters long and has at least one of each character type. The minimum number of characters to add is 1.
"""
import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    num = [i for i in "0123456789"]
    low = [i for i in "abcdefghijklmnopqrstuvwxyz"]
    upp = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    spe = [i for i in "!@#$%^&*()-+"]
    
    num_count = 0
    low_count = 0
    upp_count = 0
    spe_count = 0
    
    for i in password:
        if i in num:
            num_count+=1
        elif i in low:
            low_count+=1
        elif i in upp:
            upp_count+=1
        elif i in spe:
            spe_count+=1
            
    req_count = 0
    if num_count==0:
        req_count+=1
    if low_count==0:
        req_count+=1
    if upp_count==0:
        req_count+=1
    if spe_count==0:
        req_count+=1
    
    minimum_char = max(req_count, (6-len(password)))
    
    return minimum_char
    
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
