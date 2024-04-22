"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
a = float(input("enter an number:"))
b = float(input("enter an number:"))
c = input(" is one of the numbers is the hypotenuse of a right triangle if they are write the number again here:")

if c!=b and c!=a:
    print((a**2 + b**2)**0.5)
elif c==b:
    print((b**2 - a**2)**0.5)
elif c==a:
    print((a**2 - b**2)**0.5)

 
