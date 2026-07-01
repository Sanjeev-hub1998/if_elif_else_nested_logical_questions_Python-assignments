"""
code = int(input("Movies related code:-\n1 for child movies\n2 for Teenager movies\n3 for Adult movies\n4 for Senior citizen movies\nEnter the code here: "))
tickets = int(input("How much tickets you want?: "))
age = int(input("Enter your age: "))
time = float(input("Enter your slot time: "))
if age>=3 and age<=12 and code==1:
    if time==10 or time==11 or time==12 or time==1:
        print(f"Your ticket price is 150rs per person\nDiscount on ticket is 40%\nYour total payment is: {int(150*tickets)*0.6}")
    else:
        if time==2 or time==3 or time==4: 
            print(f"Your ticket price is 200rs per person\nDiscount on ticket is 25%\nYour total payment is: {int(200*tickets)*0.75}")
        else:
            if time==6 or time==7 or time==8 or time==9 or time==10:
                print(f"Your ticket price is 300rs per person\nDiscount on ticket is 20%\nYour total payment is: {int(300*tickets)*0.8}")

elif age>=13 and age<=19 and code==2:
    if time==10 or time==11 or time==12 or time==1:
        print(f"Your ticket price is 150rs per person\nDiscount on ticket is 40%\nYour total payment is: {int(150*tickets)*0.6}")
    else:
        if time==2 or time==3 or time==4: 
            print(f"Your ticket price is 200rs per person\nDiscount on ticket is 25%\nYour total payment is: {int(200*tickets)*0.75}")
        else:
            if time==6 or time==7 or time==8 or time==9 or time==10:
                print(f"Your ticket price is 300rs per person\nDiscount on ticket is 20%\nYour total payment is: {int(300*tickets)*0.8}")

elif age>=20 and age<=60 and code==3:
    if time==10 or time==11 or time==12 or time==1:
        print(f"Your ticket price is 150rs per person\nDiscount on ticket is 40%\nYour total payment is: {int(150*tickets)*0.6}")
    else:
        if time==2 or time==3 or time==4: 
            print(f"Your ticket price is 200rs per person\nDiscount on ticket is 25%\nYour total payment is: {int(200*tickets)*0.75}")
        else:
            if time==6 or time==7 or time==8 or time==9 or time==10:
                print(f"Your ticket price is 300rs per person\nDiscount on ticket is 20%\nYour total payment is: {int(300*tickets)*0.8}")

elif age>60 and code==4:
    if time==10 or time==11 or time==12 or time==1:
        print(f"Your ticket price is 150rs per person\nDiscount on ticket is 40%\nYour total payment is: {int(150*tickets)*0.6}")
    else:
        if time==2 or time==3 or time==4: 
            print(f"Your ticket price is 200rs per person\nDiscount on ticket is 25%\nYour total payment is: {int(200*tickets)*0.75}")
        else:
            if time==6 or time==7 or time==8 or time==9 or time==10:
                print(f"Your ticket price is 300rs per person\nDiscount on ticket is 20%\nYour total payment is: {int(300*tickets)*0.8}")

else:
    print("Your age and code is mismatched,please try again!")

"""