"""
Write a program that asks the user for a year and checks if it is a leap year.

Use logical operators to check the conditions for a leap year.

A leap year is divisible by 4, but not divisible by 100, except for years that are divisible by 400.

Requirements:
The program must ask the user to input a year and store this value in a variable.
The program must check if the entered year is divisible by 4 and use this condition in a logical operator.
The program must check if the entered year is not divisible by 100 and use this condition in a logical operator.
The program must check if the entered year is divisible by 400 and use this condition in a logical operator.
The program must output to the user whether the entered year is a leap year or not based on the performed checks.
"""

# ask the user for year
year = int(input("Enter a year: "))

#check if it is a leap year

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap Year")

else:
    print("Not Leap Year")