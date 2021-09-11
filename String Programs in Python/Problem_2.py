# problem 2
# WAP to fill in a letter template given below with name and date.
#  letter = ''' Dear<NAME>,
#           you are selected!
#          <Date>

#  from typing import Pattern, Set


letter = ''' Dear <|Name|>, You are selected! Date: <|Date|>'''



name = input("Enter your name\n");
date = input("Enter Date");
    
letter = letter.replace("<|Name|>",name);
letter = letter.replace("<|Date|>",date);
print(letter);
