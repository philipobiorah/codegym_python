# Pythagorean Multiplication Table

# Write a program that asks the user for a number N and outputs an N x N multiplication table using nested loops.
# The program should only output the numbers of the table.
# Example:
# 1   2   3   ...
# 2   4   6   ...
# 3   6   9   ...
# ...

# Write your code here
# asks the user for a number N



N = int(input("Enter value for N: "))
for i in range(1, N+1):
    for j in range(1, N+1):
        print(f"{i*j}", end="\t")
    print()


# using nested loops
#outputs an N x N multiplication table using nested loop