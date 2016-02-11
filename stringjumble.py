"""
stringjumble.py
Author: <your name>
Credit: <sources>

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""

#http://stackoverflow.com/questions/8266529/python-convert-string-to-list
#http://stackoverflow.com/questions/931092/reverse-a-string-in-python
#David Wilson is awesome!

String = input("Please enter a string of text (the bigger the better): ")

print('You entered "'+String+'". Now jumble it: ')

print(String[::-1])

SList = String.split()

NPrint = 0

while NPrint < len(SList):
    print(SList[NPrint-len(SList)], end=" ")
    NPrint += 1
print(SList[NPrint-len(SList)])

NPrint2 = 0

while NPrint2 <= len(SList):
    print(SList[NPrint2-len(SList)][::-1], end=" ")
    NPrint2 += 1

