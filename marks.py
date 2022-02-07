maths=int(input("Enter your math marks: "))
english=int(input("Enter your English marks:"))
kiswahili=int(input("Enter you Kiswahili marks: "))
chemistry=int(input("Enter your Chemistry marks: "))
physics=int(input("Enter your Physics marks: "))
geo=int(input("Enter your Geography marks: "))

marks=(maths+english+kiswahili+chemistry+physics+geo)/6
input("\nPlease press enter to know your marks\n")
if (marks>=70 and marks<=100):
    print("You have an A: ")
elif(marks>=60 and marks<=69):
    print("You have a B: ")   
elif(marks>=50 and marks<=59):
    print("You have a B: ")  
elif(marks>=40 and marks<=49):
    print("You have a B: ")      
else:
    print("You have failed: ")