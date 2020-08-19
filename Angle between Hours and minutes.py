#find angle between time.
import sys
def angle(h,m):
    print(" The time is:"+str(h)+":"+str(m))   
    if (1<=h<=12) and (0<=m<=60)  :  
            A=((30*h)-((11*m)/2))
            print("Angle between hours and minutes is:",A)
    else:
        try:
            print("invalid time")
            sys.exit()
        except:
            pass
print("Enter Hours in between 1 to 12") 
h=int(input("enter hours:"))
print("Enter Minutes in between 0 to 60")
m=int(input("enter minutes:"))
angle(h,m)