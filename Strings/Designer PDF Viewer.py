"""
There is a list of 26 character heights aligned by index to their letters. For example, 'a' is at index 0 and 'z' is at index 25. 
There will also be a string. Using the letter heights given, determine the area of the rectangle highlight in mm2 assuming all letters are 1 mm wide.

Example
h = [1,3,1,3,1,4,1,3,2,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5] 
word = 'torn'
The Heights are 
t = 2
o = 1
r = 1
n = 1
Tallest of letter is 2 high and there are 4 letters hence area is 4*2=8 so return 8

"""

def designerPdfViewer(h, word):
    arr = [getIndex(h,i) for i in word]
    maxi = max(arr)
    
    return maxi*len(word)
    
def getIndex(h, s):
    ind = ord(s)-97
    return h[ind]