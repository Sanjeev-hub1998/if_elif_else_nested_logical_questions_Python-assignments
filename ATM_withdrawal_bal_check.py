"""
Question-> Create an ATM withdrawal program with balance checks. 

balance_in_account = 2500000
PIN = 1212
PIN_1 = 2323
enter_PIN = int(input("Enter the PIN: "))

if enter_PIN==PIN:
    entered_PIN_1 = int(input("Enter the PIN to check the balance: "))
    if entered_PIN_1==PIN_1:
        print(F"Your account balance is: {balance_in_account}")
        drawing_case_1 = int(input("How much you want to waithdrawal: "))
        if balance_in_account-drawing_case_1:
            rem_bal_1 = balance_in_account-drawing_case_1
            print(f"Your account balance is: {rem_bal_1}")
            if balance_in_account<drawing_case_1:
                print("Hey,your balance is being negative,you can not withdraw!!")
            

        
        entered_PIN_1 = int(input("Enter the PIN to drawing more amount: "))
        if entered_PIN_1==PIN_1:
            drawing_case_2 = int(input("Withdrawal amount: "))
            if rem_bal_1-drawing_case_2:
                rem_bal_2 = rem_bal_1-drawing_case_2
                print(f"Your account balance is: {rem_bal_2}")
                if rem_bal_1<drawing_case_2:
                    print("Hey,your balance is being negative,you can not withdraw!!")
                    
        else:
            print("Incorrect PIN, please try again!")

                

        entered_PIN_1 = int(input("Enter the PIN to drawing more amount: "))
        if entered_PIN_1==PIN_1:
            drawing_case_3 = int(input("Withdrawal amount: "))
            if rem_bal_2-drawing_case_3:
                rem_bal_3 = rem_bal_2-drawing_case_3
                print(f"Your account balance is: {rem_bal_3}")
                print("Your transaction limit is over! Please try 24hrs later.")
                if rem_bal_2<drawing_case_3:
                    print("Hey,your balance is being negative,you can not withdraw!!")
        else:
            print("Incorrect PIN, please try again!")
    else:
        print("Incorrect PIN, please enter the balance check PIN!")

else:
    print("Incorrect PIN, please try again!")

"""