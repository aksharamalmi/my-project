grade = float(input("Enter your grade: "))

if grade >= 75:
    print("You got an A.")
elif grade >= 65:
    print("You got a B.")
elif grade >= 55:
    print("You got a C.")
elif grade >= 45:
    print("You got a D.")
else:
    print("You got an F. You need to retake the course.")
