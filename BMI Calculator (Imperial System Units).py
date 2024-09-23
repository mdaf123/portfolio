name=input("What is your name?: ")
print("Hello " + name+ "!")
weight=input("What is your weight in pounds?: ")
weight=float(weight)
height=input("What is your height in inches?: ")
height=float(height)
bmi=(weight/(height*height))*703
print("Your BMI is: " + str(bmi))
if bmi<18.5:
  print("You are underweight.")
if bmi>18.5 and bmi<25:
  print("You are average.")
if bmi>25 and bmi<30:
  print("You are overweight.")
else:
  print("You are obese.")
