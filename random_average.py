"""
Write a program that generates 10 random numbers in the range from 1 to 100 using the random library.

Then calculate their average value and print it on the screen.

Requirements:
•	The program must include the import of the random library.
•	The program must use the function random.randint(1, 100) to generate each of the 10 random numbers.
•	The program must calculate the average value of the generated numbers by summing all the numbers and dividing the result by their count (10).
•	The program must print the average value of the generated numbers on the screen
"""

# Random Average

# Write a program that generates 10 random numbers in the range from 1 to 100 using the random library.
# Then calculate their average value and print it on the screen.

# Write your code here
import random



ran_sum = 0
#generate 10 random numbers 
for i in range(10):
    #in the range from 1 to 100
    ran_sum += random.randint(1,100)

#calculate their average
ran_avg = ran_sum/10

# print it on the screen
print(ran_avg)