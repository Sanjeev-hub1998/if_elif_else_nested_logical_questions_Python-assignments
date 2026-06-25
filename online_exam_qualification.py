"""

Question -:Determine online exam qualification. 

OTP = 1212
password = "sanjeev123"
name = "Sanjeev kumar sanjeev kumar Sanjeev Kumar"
Roll_no = 123456
course = "Bcom bcom B.com b.com"
code = int(input("Enter the center code: "))
entered_password = input("Enter password: ")



if code==OTP and entered_password==password:
    print("You are logged in!\nGo ahead..\n\n")

    entered_name = input("Enter name: ")
    rollno = int(input("Enter Roll number: "))
    course_name = input("Enter the course name: ")

    if entered_name in name and rollno==Roll_no and course_name in course:
        print("\nPlease read the instructions carefully\n\nEnglish: 50 Questions and 50 Marks\nMathematics: 50 Questions and 50 Marks\nReasoning: 50 Questions and 50 Marks\nGeneral Awareness: 50 Questions and 50 Marks.\n\nCorrect Answer: +2 marks\nIncorrect Answer: -0.50 marks (negative marking)\nUnanswered: 0 marks")
    elif entered_name not in name and rollno == Roll_no and course_name in course:
        print("Please enter name correctly!")
    elif entered_name in name and rollno!=Roll_no and course_name in course:
        print("Please enter roll no. correctly!")
    else:
        print("Please enter course name correctly!")
else:
    if code!=OTP and entered_password==password:
        print("Incorrect OTP,try again!")
    else:
        print("Incorrect password,try again!")


"""