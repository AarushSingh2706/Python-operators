a = int(input("Enter your height in cm  "))
b = int(input("Enter your weight in kg  "))
BMI = b / (a / 100)**2
print("This is your BMI ", BMI)
if BMI <= 18.4 : 
    print("You are underweight")
elif BMI <=24.9 : 
    print("You are healthy")
elif BMI <=29.9 : 
    print("You are overweight")
elif BMI <= 34.9 : 
    print("You are severly overweight")
elif BMI <= 39.9 : 
    print("You are obese")
else :
    print("You are severly obese")