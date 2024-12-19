# Write program to convert the distance (in feet) to inches, yards, and miles.
# Input:
# Enter the distance in feet : 5
# Expected Output:
# Distance in feet : 5.0
# Distance in inches : 60.0
# Distance in yards : 1.6666666666666667
# Distance in miles : 0.000946969696969697

distance=float(input("Enter the distance in feet: "))
inches=distance*12
yards=distance/3
miles=distance/5280
print("Distance in feet :",distance)
print("Distance in inches :",inches)
print("Distance in yards :",yards)
print("Distance in miles :",miles)