"""
Validate strong password using multiple conditions.

entered_pass = input("Enter the password: ")
if entered_pass=="1":
    print("Type next digit..")

    entered_pass = input("Enter the password: ")
    if entered_pass=="2":
        print("Type next digit..")

        entered_pass = input("Enter the password: ")
        if entered_pass=="3":
            print("Type next digit..")
            
            entered_pass = input("Enter the password: ")
            if entered_pass=="4":
                print("You are logged in!")
            else:
                print("Incorrect password!")
else:
    print("Incorrect password!")

"""