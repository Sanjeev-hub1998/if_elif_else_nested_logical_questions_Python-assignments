"""
Question-> Write a Python program to calculate income tax using slabs. 

inc = int(input("Enter your annual income: "))
a1 = 0
a = 2.5                     #a1,a,b,c,d,e define rates on income
b = 5
c = 7.5
d = 10
e = 30
if inc<1200000:
    print(f"Your annual income is: {inc}\nRate is: {a1}%\nYou have to pay as an income tax: {inc*0}")
if inc>=1200000 and inc<1500000:
    print(f"Your annual income is: {inc}\nRate is: {a}%\nYou have to pay as an income tax: {inc*0.025}")
elif inc>=1500000 and inc<1800000:
    print(f"Your annual income is: {inc}\nRate is: {b}%\nYou have to pay as an income tax: {inc*0.05}")
elif inc>=1800000 and inc<2100000:
    print(f"Your annual income is: {inc}\nRate is: {c}%\nYou have to pay as an income tax: {inc*0.075}")
elif inc>=2100000 and inc<3000000:
    print(f"Your annual income is: {inc}\nRate is: {d}%\nYou have to pay as an income tax: {inc*0.1}")
else:
    if inc>=3000000:
        print(f"Your annual income is: {inc}\nRate is: {e}%\nYou have to pay as an income tax: {inc*0.3}")


"""