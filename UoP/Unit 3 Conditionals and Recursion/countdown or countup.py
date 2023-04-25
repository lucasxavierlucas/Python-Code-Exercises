def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)

def countdown(n):
    if n <= 0:
        print('Blastoff!')  
    else:
        print(n)
        countdown(n-1)

n = int(input('Enter a number: '))
#gets a number from the user and calls either countdown or countup depending on the input:
if n > 0:
    countdown(n)
elif n < 0:
    countup(n)
else:
    print('Blastoff!') #since the countdown function already prints "Blastoff!" for zero or negative inputs, we can reuse it for zero


'''The respective outputs for the following inputs are:

Enter a number: 5
5
4
3
2
1
Blastoff! 

Enter a number: -3
-3
-2
-1
Blastoff!

Enter a number: 0
Blastoff!

'''

