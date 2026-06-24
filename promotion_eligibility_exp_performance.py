"""

Question :- Check promotion eligibility using experience and performance. 

print("exp==1 and per==1--------1.Data Entry,2.Sales & Marketing\nexp>1 and exp<=3 and per==2----1.Administrative,2.Accounting\nexp>3 and exp<=5 and per==3-----1.1.Finance & HR,2.Technical & Support\nexp>5 and exp<=10 and per==4-----1.Supervisor,2.Project Manager\nexp>10 and per==5-----1.Managing Director,2.Department Managers.\n\nAll conditions have been given,Please chose wisely!\n")
exp = int(input("Enter your experience: "))
per = int(input("Give star to Performance from 1 to 5: "))
if exp==1 and per==1:
    print("Your option is:\n1.Data Entry\n2.Sales & Marketing\nChose wisely!\n")
    de = input("Select the one from the given choice: ")
    if de=="Data Entry":
        print("Congratulations! You have been promoted on Data Entry role.")

    if de=="Sales & Marketing":
        print("Congratulations! You have been promoted on Sales & Marketing role.")

elif exp>1 and exp<=3 and per==2:
     print("Your option is:\n1.Administrative\n2.Accounting\nChose wisely!\n")
     de = input("Select the one from the given choice: ")
     if de=="Administrative":
        print("Congratulations! You have been promoted on Administrative role.")

     if de=="Accounting":
        print("Congratulations! You have been promoted on Accounting role.")

elif exp>3 and exp<=5 and per==3:
     print("Your option is:\n1.Finance & HR\n2.Technical & Support\nChose wisely!\n")
     de = input("Select the one from the given choice: ")
     if de=="Finance & HR":
        print("Congratulations! You have been promoted on Finance & HR role.")

     if de=="Technical & Support":
        print("Congratulations! You have been promoted on Technical & Support role.")

elif exp>5 and exp<=10 and per==4:
     print("Your option is:\n1.Supervisor\n2.Project Manager\nChose wisely!\n")
     de = input("Select the one from the given choice: ")
     if de=="Supervisor":
        print("Congratulations! You have been promoted on Supervisor role.")

     if de=="Project Manager":
        print("Congratulations! You have been promoted on Project Manager.")

elif exp>10 and per==5:
     print("Your option is:\n1.Managing Director\n2.Department Managers\nChose wisely!\n")
     de = input("Select the one from the given choice: ")
     if de=="Managing Director":
        print("Congratulations! You have been promoted on Managing Director role.")

     if de=="Department Managers":
        print("Congratulations! You have been promoted on Department Managers.")

else:
    print("Incorrect!,please enter correctly!")

"""