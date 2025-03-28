 # Height in Feet and Inches

# Write a program that converts the user's height, given in centimeters, into feet and inches.
# The height value is given in the variable height_cm. One inch is equal to 2.54 cm, and one foot is equal to 12 inches.
# Your task is to calculate the number of complete feet in the given height and convert the remainder into inches.
# Display the result on the screen.

height_cm =  float(input("Enter user height in cm : "))
print(height_cm)


cm_per_inch = 2.54
inch_per_foot = 12


# calculate the number of complete feet in the given height cm

# convert height cm to inches
inches = height_cm / cm_per_inch
complete_foot = inches // inch_per_foot

rem_inches = inches % inch_per_foot

print(complete_foot, "'", rem_inches) 


