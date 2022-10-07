# Ask user to input email and check if the email is in valid form or not. Ex: it should contain single '@', '.', @or.shouldn't be in 1st position
import re

def solve(s):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,s):
      return True
   return False

s = str(input("Enter valid email id: "))
print(solve(s))
