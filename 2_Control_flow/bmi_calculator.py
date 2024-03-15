height = float(input("What is your height\n"))
weight = int(input("What is your weight\n"))
# weight_as_int = int(weight)
# height_as_float = float(height)
# bmi = weight_as_int / height_as_float ** 2
bmi = int(weight / height ** 2)
# bmi_as_int = int(bmi)
print(bmi)

if bmi < 18.5:
    print(f"you bmi is {bmi} you are under weight")
elif bmi < 25:
    print(f"You have normal weight {bmi}")
elif bmi < 30:
    print(f"Your BMI is {bmi} slightly overweight")
elif bmi < 35:
    print(f"You bmi is {bmi} you are obese")
else:
    print(f"Your Bmi is {bmi} you are clinically obese")