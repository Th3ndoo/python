# exam eligability test
mc = input("Student have medical cause or not(y/n)")

if mc == "y":
    print("the student is allowed to write the exam")
else:
    att = int(input("enter the attendance of the student"))
    if att > 75:
        print("students are allowed to write the exam")
    else:
        print("student are not allowed to write the exam")