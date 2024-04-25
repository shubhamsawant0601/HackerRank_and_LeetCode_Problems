"""
771. Jewels and Stones

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have.  You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".


Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:

Input: jewels = "z", stones = "ZZ"
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Define list of characters for jewels and stones
        count = 0
        stones = list(stones)
        jewels = list(jewels)
        
        # Check each character of jewel for its count in stones and increament count
        for i in jewels:
            count += countFreq(stones, i)
        
        # Return count
        return count
           
# Define function which calculate count of character in given string
def countFreq(string, char):
    count = string.count(char)
    return count
    