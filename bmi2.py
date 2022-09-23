height = float(input("Please enter your height in meters: "))
weight = float(input("Please enter your weight in kilograms: "))
bmi1 = weight/height**2
bmi = round(bmi1)
if bmi < 18.5:
    print("Your BMI is " + str(bmi) + ". You are underweight.")
elif bmi < 25:
    print("Your BMI is " + str(bmi) + ". You are a normal weight.")
elif bmi < 28:
    print("Your BMI is " + str(bmi) + ". You are slightly overweight.")
elif bmi < 31:
    print("Your BMI is " + str(bmi) + ". You are overweight.")
elif bmi < 35:
    print("Your BMI is " + str(bmi) + ". You are obese.")
else:
    print("Your BMI is " + str(bmi) + ". You are clinically obese.")
