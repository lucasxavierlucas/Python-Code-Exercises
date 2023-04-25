#Description: My functions discover if the input number is even or odd and prints the result in the output. 

def even_or_odd(n):
    if n % 2 == 0: # check if the number is even
        return "This number is even"
    else:
        return "This number is odd" # return if the number is odd

print(even_or_odd(4))  # output: "This number is even"
print(even_or_odd(7))  # output: "This number is odd"
print(even_or_odd(0))  # output: "This number is even"
