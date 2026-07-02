"""
pin = 1234
entered_pin = int(input("Enter the PIN: "))
if entered_pin==pin:
    amount = int(input("Enter the amount: "))

    if amount<0:
        print("Account Type: Negative Account")

    elif amount<100 and amount>=0:
        print("Account Type: Basic Account\nBalance Range: 100rs to very low\nFeatures: No Monthly Average Balance (MAB) requirements. Usually designed for students, basic salary accounts, or financial inclusion programs.\nLimitations: May limit the number of free monthly ATM withdrawals or branch transactions.Bank example: Axis Bank")
    
    elif amount>=100 and amount<=10000:
        print("Account Type: Regular / Standard Accounts\nBalance Range: Low to moderate (e.g., maintain 100rs - 2,500rs or local equivalent)\nFeatures: Standard checking and savings accounts used for everyday spending and building a safety net.\nLimitations: Banks charge a penalty or maintenance fee if the account drops below the required minimum balance.\nBank example: ICICI Bank")

    elif amount>10000 and amount<=50000:
        print("Account Type: High-Yield Savings & Money Market Accounts\nBalance Range: Moderate to High (e.g., 10,000rs and above)\nFeatures: Best for parkings funds you want to grow. These accounts offer significantly higher interest rates than regular accounts and are a hybrid between savings and checking.\nLimitations: Usually require a higher minimum initial deposit and might limit the number of withdrawals per month.\nBank example: Mid Penn Bank")

    else:
        print("Account Type: Premium / Priority Accounts\nBalance Range: High (e.g., 50,000rs plus)\nFeatures: Designed for high-net-worth individuals. Benefits include dedicated relationship managers, waived wire fees, preferential loan rates, and free unlimited ATM usage worldwide.\nLimitations: If your balance dips below the required high threshold, you will be downgraded to a standard account tier and lose premium perks.Bank example: Canara Bank")

else:
    print("PIN is not matched,enter the PIN again!")

"""