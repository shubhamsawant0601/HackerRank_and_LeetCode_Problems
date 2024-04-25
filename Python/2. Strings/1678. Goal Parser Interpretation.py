"""
1678. Goal Parser Interpretation

You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".

Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"

Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"

"""

class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("G", "G")
        command = command.replace("()", "o")
        command = command.replace("(al)", "al")
        
        return command
    

"""------------------------------OR----------------------------------------"""
class Solution:
    def interpret(self, command: str) -> str:
        command = replace(command, "()", "o")
        command = replace(command, "(al)", "al")
        command = replace(command, "G", "G")
        
        return command
        
        
# making own replace function 
# Split string across old character, which removes old characters
# Join list of Characters with new character as joining characters

def replace(string, str1, str2):
    s1 = string.split(str1)
    s2 = str2.join(s1)
    
    return s2