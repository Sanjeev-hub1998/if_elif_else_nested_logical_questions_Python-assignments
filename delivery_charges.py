"""

Question:- Calculate delivery charges based on location and order amount. 


location_1 = "Delhi"
location_2 = "Noida"
location_3 = "Ghaziabad"
order = int(input("Enter your order amount: "))
location = input("Enter your location: ")
charges_1 = "25%"
charges_2 = "20%"
charges_3 = "15%"
if order>=200:
    if order>=200 and location==location_1:
        print(f"Your order amount:{order}\nCharges on order is:25%\nYour charges amount on order is:{order*0.25}")
    elif order>=200 and location==location_2:
        print(f"Your order amount:{order}\nCharges on order is:20%\nYour charges amount on order is:{order*0.20}")
    elif order>=200 and location==location_3:
        print(f"Your order amount:{order}\nCharges on order is:15%\nYour charges amount on order is:{order*0.15}")

    elif order>=200 and (location!=location_1 or location!=location_2 or location!=location_3):
        print("Location is wrong!,please enter correctly.")


else:
    if order<200 and (location==location_1 or location==location_2 or location==location_3):
        print("Your purchasing order is rejected.\nYour purchasing amount should be minimum: 200rs")
    else:
        if order<200 and (location!=location_1 or location!=location_2 or location!=location_3):
            print("Your purchasing amount should be minimum: 200rs,also give correct location.")


"""