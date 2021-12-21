print("Hello I am a BMI calculator!")

weight = int(input("What's your weight (in Kg)? \n >"))
height = int(input("What's height (in Metres)? \n >"))

def bmi(height, weight):
    beemi = (weight) / (height * height)
    return beemi

UserBMI = round(bmi(height, weight)*10000, 1)

print("Alright your BMI is {}".format(UserBMI))

if UserBMI < 18.5:
    print("You are underweight!")

if UserBMI >= 18.5 and UserBMI < 25:
    print("You are healthy!")

if UserBMI >= 25 and UserBMI < 30:
    print("You are overweight!")

if UserBMI > 30:
    print("You are obese!!!")
