"""
Sample Input

saveChangesInTheEditor
Sample Output

5
Explanation

String  contains five words:

save
Changes
In
The
Editor
"""

import math
import os
import random
import re
import sys


def camelcase(s):
    # Write your code here
    count =  1
    for i in s:
        if 64<ord(i)<91:
            count += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
