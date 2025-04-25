
# Ternary Operator

# Write a program that asks the user for a number and uses the ternary operator to check whether it is even or odd.
# Display the appropriate message.

# Write your code here
#ask user for input
number = int(input("Enter a number: "))

#use the ternary operator to check whether it is even or odd.
output = "even" if number % 2 == 0  else "odd"

#display
print(output)