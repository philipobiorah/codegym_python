"""

Write a program that asks the user for a number and uses the math library to calculate and display the square root and factorial of that number.

Requirements:
•	The program must include an import of the math library.
•	The program must ask the user to input a number.
•	The program must use the sqrt function from the math library to calculate the square root of the entered number.
•	The program must use the factorial function from the math library to calculate the factorial of the entered number.
•	The program should output the calculation results (the square root and factorial) to the screen.

"""

import math

#ask the user to input a number.

num = int(input("Enter a number : "))


#use the sqrt function from the math library to calculate the square root of the entered number.
num_square = math.sqrt(num)

#calulate the factorial of the number
# 5 factorial is 5! = 5 x 4 x 3 x 2 x 1 = 120
# 0 factorial is a definition: 0! = 1. There is exactly 1 way to arrange 0 objects

num_fac = 1
for i in range(1, num + 1):
    num_fac *= (num + 1 - i)

print(f'Factorial: {num_fac}')


#using the math fucntion math.factorial(x)
# num_fac = math.factorial(num)