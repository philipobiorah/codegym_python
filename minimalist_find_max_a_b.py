# Maximalist

# Write a function find_max(a, b) that takes two numbers as arguments and returns the greater of them.
# If the numbers are equal, the function should return either.
# Then write a program that prompts the user for two numbers, calls this function, and prints the result.

# Write your code here


a = int(input("Enter first number: "))
b = int(input("Enter Second number: "))


def find_max(a,b):
    return a if a > b else b
    

print(find_max(a, b))