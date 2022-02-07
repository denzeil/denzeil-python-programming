a=int(input("Enter  A:"))
b=int(input("Enter  B: "))
c=int(input("Enter  C:"))

if (a>b and a>c):
    print("A is the largest")
if(a>b and b>c):
    print("B is the largest") 
elif(c>a and c>b):
    print("C is the largest")      
