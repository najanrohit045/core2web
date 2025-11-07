angle1=int(input("Enter a angle1:"))
angle2=int(input("Enter a angle2:"))
angle3=int(input("Enter a angle3:"))

if ((angle1==90 or angle2==90 or angle3==90) and angle1+angle2+angle3==180):
    print("Its a right angle triangle")
else:
    print("it is not a right angle triangle")
