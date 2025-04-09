# BMI checker

w = float(input("enter the weight in kgs"))
h = float(input("enter the height in meters"))

bmi = w/(h*h)

if bmi < 18.5:
    print("you are underweight")
elif bmi < 25:
    print("you are healthy")
elif bmi < 30:
     print("you are overweight")
elif bmi < 35:
    print("you are obese")
else :
    print("you are extremely obese2")
