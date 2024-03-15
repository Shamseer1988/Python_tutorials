print("The love calculator")

name1 = input("What is your name")
name2 = input("What is you their name")

merged_name = name1 + name2

lower_name = merged_name.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

first_digit = t + r + u + e
print(first_digit)
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
second_digit = l + o + v + e
print(l)
score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
    print(f"Your score is {score}")
elif (score >= 40) or (score <= 50):
    print(f"Your Score is {score}")
else:
    print(f"urScore is {score}")
