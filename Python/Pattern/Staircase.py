"""
Staircase detail

This is a staircase of size 4:

   #
  ##
 ###
####

Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .
"""


def staircase(n):
    for i,j in zip(range(1,n+1), range(n-2, -1, -1)):
        print(" "*j, "#"*i)
    
    print("#"*n)
