"""
Sample Input 0

5
47
Sample Output 0

thirteen minutes to six
Sample Input 1

3
00
Sample Output 1

three o' clock
Sample Input 2

7
15
Sample Output 2

quarter past seven

"""

def timeInWords(h, m):
    
    num = ["zero", "one", "two","three", "four", "five","six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    
    twenty = ["twenty "+num[i] for i in range(1,10,1)]
    
    num = num + twenty
    
    if m==0:
        return str(num[h]+ " o' clock")
    
    if m==1 :
        return str(num[m]+" minute past "+num[h])
    
    if m==30:
        return str("half past "+num[h])
    
    if m==15:
        return str("quarter past "+num[h])
    
    if m==45:
        return str("quarter to "+num[h+1])
    
    if m<30 :
        return str(num[m]+" minutes past "+num[h])
    
    if m>30 :
        return str(num[60-m]+" minutes to "+ num[h+1])
    
    