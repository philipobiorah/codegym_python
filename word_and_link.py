# A Word and a Link

# Write a program that creates two lists, assigns one of them to another variable, and checks if both variables point to the same object.
# Use the is operator to check the references.

# Write your code here

lista = [1, 3, None, 5]

listb = lista

if lista is listb:
    print("same object")
else:
    print("differnet object")