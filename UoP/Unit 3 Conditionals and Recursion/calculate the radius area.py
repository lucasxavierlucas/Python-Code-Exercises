pi = 3.14159 # Define pi


def print_volume(r):
    volume = (4/3) * pi * r ** 3 # Calculate the volume
    print("The volume of a sphere with radius", r, "is:", volume)

# Call the function with different radius values
print_volume(2) # Output: The volume of a sphere with radius 2 is: 33.51029333333333
print_volume(5) # Output: The volume of a sphere with radius 5 is: 523.5983333333332
print_volume(10) # Output: The volume of a sphere with radius 10 is: 4188.786666666666