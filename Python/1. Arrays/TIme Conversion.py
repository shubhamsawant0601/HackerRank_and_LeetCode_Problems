"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example

s = "12:01:00PM"
Return '12:01:00'.

s = "12:01:00AM"
Return '00:01:00'.

"""



def timeConversion(s):
    zone = s[-2:]
    li = s[:-2].split(":")
    
    if zone == "AM":
        if li[0] == "12":
            li[0] = "00"
            
        s = ":".join(li)
        
    else:
        if li[0] != "12":
            li[0] = str(int(li[0])+12)
            
        s = ":".join(li)
        
    return s