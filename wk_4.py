weight = float(input("Your weight: "))
height = float(input("Your height: "))


def BMI(weight, height):
    height = height * height
    print("BMI calculator: ", weight/height)


BMI(weight, height)
