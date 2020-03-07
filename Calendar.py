import calendar
import datetime
import time
#Take Year as input
n=int(input("Enter your desired year: "))
print(calendar.calendar(n))
leapYear=calendar.isleap(n)
if(leapYear):
    print("\n\n##This is Leap Year :)")
print("\n\n***If you want to see the specific month of a year,you can enter your desired year and month here***")
n=int(input("\nEnter your desired year-> "))
m=int(input("Enter number of month->"))
print(calendar.month(n,m))
print("\n\n***How many leapdays in years***")
n1=int(input("Enter first year:"))
n2=int(input("Enter last year:"))
print(calendar.leapdays(n1,n2))
print("\n\n##You can know the day of any date##")
y=int(input("Enter any year-->"))
m=int(input("Enter any month-->"))
d=int(input("Enter any date-->"))
r=calendar.weekday(y,m,d)
if(r==0):
    print("Monday")
elif(r==1):
    print("Tuesday")
elif(r==2):
    print("Wednesday")
elif(r==3):
    print("Thursday")
elif (r==4):
    print("Friday")
elif(r==5):
    print("Saturday")
elif(r==6):
    print("Sunday")
