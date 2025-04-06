# The Clever Raja

# Write a program that calculates how many grains of wheat will be on each square of a chessboard,
# if one grain is placed on the first square, two grains on the second square, four grains on the third square, and so on.
# There are a total of 64 squares on the chessboard.
# Use a for loop and the range() function to iterate over the squares and the print() function to display the result.
# Example:
# For the first three squares, the program should output:
# Square 1: 1 grain
# Square 2: 2 grains
# Square 3: 4 grains
# ...

# Write your code here
for i in range(0, 63):
    print("Square ",i+1,":", 2**i," grain")