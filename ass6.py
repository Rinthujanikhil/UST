#Ask user a input string and check if the entered string is palindrome. Ex: Input NitiN -> o/p palindrome
def palindrome():
  word=str(input("Enter the string:"))
  reverse_String=word[::-1]
  print(reverse_String)
  if(reverse_String==word):
    print("Word is a palindrom")
  else:
      print("Not a Palindrom")


palindrome()          
