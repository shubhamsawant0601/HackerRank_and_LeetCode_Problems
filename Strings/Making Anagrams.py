import math
import os
import random
import re
import sys
from collections import Counter


def makeAnagram(a, b):
    # Write your code here
    count_a = Counter(a)
    count_b = Counter(b)
    
    diff1 = count_a - count_b
    diff2 = count_b - count_a

    return sum(diff1.values())+sum(diff2.values())



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = input()
    b = input()
    res = makeAnagram(a, b)
    fptr.write(str(res) + '\n')
    fptr.close()
