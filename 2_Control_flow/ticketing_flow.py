print("Welcome to the rollercoaster")
height = int(input("What is you height in CM"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age ? "))
    if age <= 12:
        bill = 5
        print("Child ticket $5")
    elif age <= 18:
        bill = 7
        print("youth ticket $7")
    else:
        print("Adult ticket $12")
        bill = 12
    wants_photo = input("Do you want to Photo Y or N").lower()
    if wants_photo == "y":
        bill += 3
    print(f"Your Bill is {bill}")

else:
    print("Sorry , you are unable to ride the rollercoaster")
