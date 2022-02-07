salary=float(input("What is your salary: "))
years=int(input("Years of service: "))
if (years>10):
    total=salary*1.1
    print("Your net bonus is: ",total)
elif(years>=6 and years<=10):    
    total=salary*1.08
    print("Your net bonus is",total)
elif(years<6):
    total=salary*1.05
    print("Your net bonus is: ",total)    