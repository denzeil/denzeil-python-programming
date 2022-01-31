citizen=input("Are you a kenyan citizen: Yes or no ").lower()
age=int(input("What is your age: "))
if(citizen=="Yes" and age>=18):
    print("You can vote")
elif(citizen=="no" or age>=18):
    print("You can still vote:")
else:
      print("You can't vote")