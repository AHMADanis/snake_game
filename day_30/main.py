height = float(input("height: "))
weight = int(input("weight: "))


if height > 3:
    raise ValueError("human over height")

bmi = weight / (height * height)
print(bmi)
