#Enter the total amount of goods
#if the amount is more than a 1000 then the  discount is 5%
#or else no discount
Amount=float(input("Enter the amount : "))
if (Amount>=1000):
    print("Your amount is: ",Amount*0.05)
else:
    print("You don't have a discount",Amount)    