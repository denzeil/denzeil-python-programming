a=int(input("Enter height A:"))
b=int(input("Enter height B: "))
c=int(input("Enter height C:"))

if (a>b and a>c):
    print("A is the tallest")
elif(b>a and b>c):
    print("B is the tallest") 
elif(c>a and c>b):
    print("C is the tallest")      
