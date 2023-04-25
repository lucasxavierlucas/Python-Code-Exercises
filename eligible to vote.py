# This program asks the user for their age and prints a message based on their age

'''
age = input("Please enter your age: ")
if age < 18:
    print("You are not old enough to vote.")
else:
    print("You are eligible to vote.")'''

#So basically, the program is asking for my age but then trying to compare a string to an integer, which doesn't work. 
#That's why it's throwing a TypeError. I need to fix the code to compare integers instead of strings.

#We gotta use int() to turn age into a number so we can compare it properly.
age = int(input("Please enter your age: "))
if age < 18:
    print("You are not old enough to vote.")
else:
    print("You are eligible to vote.")

'''
output: 
Please enter your age: 27
You are eligible to vote.

'''