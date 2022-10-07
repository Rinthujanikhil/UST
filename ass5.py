#Python is a widely used general-purpose, high level programming language. It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code"""


#calculate the number of vowels individually i.e number of a, e, i , o and u , calculate total number of consonants without considering any punctuation character

String="""Python is a widely used general-purpose, high level programming language.
It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation.
It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code"""

print("count number of a from the string",String.count('a')+String.count('A')) #counting
print("count number of e from the string",String.count('e')+String.count('E'))
print("count number of i from the string",String.count('i')+String.count('I'))
print("count number of o from the string",String.count('o')+String.count('O'))
print("count number of u from the string",String.count('u')+String.count('U'))
vowels=0
consonants=0
for i in String:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u'):
        vowels=vowels+1;
    else:
        consonants=consonants+1;
 
print("The number of vowels:",vowels);
print("\nThe number of consonant:",consonants);

